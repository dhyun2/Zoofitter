// ESLint 기본 추천 규칙 및 TypeScript 스타일 가이드
import js from "@eslint/js";
import tseslint from "@typescript-eslint/eslint-plugin";
import tsparser from "@typescript-eslint/parser";
import airbnbTs from "eslint-config-airbnb-typescript"; // TypeScript 스타일 가이드 유지
import prettier from "eslint-config-prettier";
import importPlugin from "eslint-plugin-import";

export default [
  // 기본 ESLint 추천 규칙 적용
  js.configs.recommended,

  // Airbnb TypeScript 스타일 가이드 적용 (React 미포함)
  airbnbTs,

  // Prettier와 충돌하는 규칙 해제
  prettier,

  {
    // ESLint가 무시할 파일 및 폴더 설정
    ignores: ["node_modules/", "dist/", "build/", "**/*.min.js"],

    // TypeScript 지원을 위한 언어 설정
    languageOptions: {
      parser: tsparser, // TypeScript 파서 적용
      parserOptions: {
        ecmaVersion: "latest", // 최신 ECMAScript 문법 지원
        sourceType: "module", // ES 모듈 사용
        project: "./packages/ts-config/tsconfig.base.json", // TypeScript 프로젝트 설정 참조
      },
    },

    // ESLint에서 사용할 플러그인 정의
    plugins: {
      import: importPlugin, // 모듈 import 관련 규칙 제공
      "@typescript-eslint": tseslint, // TypeScript 지원을 위한 플러그인
    },

    // 적용할 규칙 설정
    rules: {
      ...importPlugin.configs.errors.rules, // import 관련 에러 규칙 적용
      ...importPlugin.configs.warnings.rules, // import 관련 경고 규칙 적용
      ...importPlugin.configs.typescript.rules, // TypeScript 관련 import 규칙 적용
      "prettier/prettier": "error", // Prettier 규칙 강제 적용
    },
  },
];
