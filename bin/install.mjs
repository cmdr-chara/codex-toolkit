#!/usr/bin/env node

import { cp, mkdir, rename, stat } from "node:fs/promises";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const packageRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const codexHomeArg = process.argv.indexOf("--codex-home");
const codexHome = codexHomeArg >= 0
  ? process.argv[codexHomeArg + 1]
  : process.env.CODEX_HOME || join(homedir(), ".codex");

if (!codexHome || (codexHomeArg >= 0 && !process.argv[codexHomeArg + 1])) {
  throw new Error("--codex-home requires a path");
}

const stamp = new Date().toISOString().replace(/[:.]/g, "-");
const backupRoot = join(codexHome, "backups", `mission-control-${stamp}`);
const skillName = "delegate-with-mission-cards";
const skillSource = join(packageRoot, "skills", skillName);
const skillTarget = join(codexHome, "skills", skillName);
const agentSource = join(packageRoot, "agents", "mission-control");
const agentTarget = join(codexHome, "agents");

async function exists(path) {
  try {
    await stat(path);
    return true;
  } catch (error) {
    if (error.code === "ENOENT") return false;
    throw error;
  }
}

async function backup(path, relativeTarget) {
  if (!(await exists(path))) return false;
  const destination = join(backupRoot, relativeTarget);
  await mkdir(dirname(destination), { recursive: true });
  await rename(path, destination);
  return true;
}

await mkdir(agentTarget, { recursive: true });
let createdBackup = await backup(skillTarget, join("skills", skillName));
await mkdir(dirname(skillTarget), { recursive: true });
await cp(skillSource, skillTarget, { recursive: true });

const agentNames = [
  "pathfinder-reader.toml",
  "patcher-writer.toml",
  "investigator-reader.toml",
  "builder-writer.toml",
  "sentinel-reader.toml",
  "architect-writer.toml"
];

for (const name of agentNames) {
  const target = join(agentTarget, name);
  createdBackup = (await backup(target, join("agents", name))) || createdBackup;
  await cp(join(agentSource, name), target);
}

console.log(`Mission Control installed in ${codexHome}`);
if (createdBackup) console.log(`Previous files backed up to ${backupRoot}`);
console.log("Start a fresh Codex task to load the skill and agents.");
