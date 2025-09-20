import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import dts from "vite-plugin-dts";
import path from "path";

export default defineConfig({
  plugins: [
    vue(),
    dts({
      insertTypesEntry: false,
      include: ["src/**/*.ts"],
      skipDiagnostics: true,
      outDir: "dist/types",
      copyDtsFiles: true,
      tsConfigFilePath: path.resolve(__dirname, "tsconfig.json")
    })
  ],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src")
    }
  },
  build: {
    lib: {
      entry: path.resolve(__dirname, "src/index.ts"),
      name: "Globaltechia",
      fileName: (format) => `globaltechia.${format}.js`
    },
    rollupOptions: {
      external: ["vue","vue-router"],
      output: {
        globals: {
          vue: "Vue"
        }
      }
    }
  }
});