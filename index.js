const fs = require("fs");
const path = require("path");
const chalk = require("chalk");

function readPackageVersion(moduleId) {
  const entryPath = require.resolve(moduleId);
  const manifestPath = path.join(path.dirname(entryPath), "package.json");
  return JSON.parse(fs.readFileSync(manifestPath, "utf8")).version;
}

const rootAnsiStylesVersion = readPackageVersion("ansi-styles");
const chalkAnsiStylesVersion = readPackageVersion("chalk/node_modules/ansi-styles");

console.log(chalk.green("example_dep_repo JS dependency demo"));
console.log(`root ansi-styles version: ${rootAnsiStylesVersion}`);
console.log(`chalk nested ansi-styles version: ${chalkAnsiStylesVersion}`);
