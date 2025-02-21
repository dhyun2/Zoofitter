export default {
  bracketSpacing: true,
  bracketSameLine: true,
  singleQuote: true,
  semi: true,
  tabWidth: 2,
  useTabs: false,
  trailingComma: "all",
  printWidth: 120,
  arrowParens: "always",
  endOfLine: "auto",
  importOrder: [
    "(.*)/__mocks__/(.*)",
    "^@lib/(.*)$",
    "^@components/(.*)$",
    "^@(server|trpc)/(.*)$",
    "^~/(.*)$",
    "^[./]",
  ],
  importOrderSeparation: true,
  plugins: ["@trivago/prettier-plugin-sort-imports"],
};
