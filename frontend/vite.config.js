import { defineConfig } from 'vite'
import { resolve } from 'path' // 主要用于alias文件路径别名
import vue from '@vitejs/plugin-vue'
// 下面这三行是引入组件
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import viteCompression from 'vite-plugin-compression'
function pathResolve(dir) {
  return resolve(__dirname, '.', dir)
}
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // 自动引入组件和自动注册 new add
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
    // 配置 gzip 压缩插件
    viteCompression({
      // options
      verbose: true, // 是否在控制台输出压缩结果
      disable: false, // 是否禁用
      threshold: 1024 * 10, // 压缩的门槛大小
      algorithm: 'gzip', // 压缩的算法
      ext: '.gz', // 压缩后的文件扩展名
    }),
  ],
  // 这里是将src目录配置别名为 /@ 方便在项目中导入src目录下的文件
  resolve: {
    alias: {
      '/@': pathResolve('src'),
    },
  },
  define: {
    'process.env': {},
  },
  // 强制预构建插件包
  optimizeDeps: {
    include: ['axios'],
  },
  base: './',
  // 打包配置
  build: {
    publicDir: '',
    target: 'modules',
    outDir: 'dist', //指定输出路径
    assetsDir: 'assets', // 指定生成静态资源的存放路径
    minify: 'terser', // 混淆器，terser构建后文件体积更小
    rollupOptions: {
      output: {
        // 对静态资源进行单独打包
        assetFileNames: 'static/[ext]/[name].[hash].[ext]',
        // 对项目依赖进行单独打包
        manualChunks: (id) => {
          if (id.includes('node_modules')) {
            return 'vandor'
          }
        },
      },
    },
    terserOptions: {
      compress: {
        //生产环境时移除console
        drop_console: true,
        drop_debugger: true,
      },
    },
  },
  server: {
    host: '0.0.0.0',
    cors: true, // 默认启用并允许任何源
    open: true, // 在服务器启动时自动在浏览器中打开应用程序
    //反向代理配置，注意rewrite写法，开始没看文档在这里踩了坑
    proxy: {
      '/api': {
        target: 'http://192.168.99.223:3000', //代理接口
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
