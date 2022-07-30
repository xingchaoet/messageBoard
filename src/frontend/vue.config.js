module.exports = {
  devServer:{
    // proxy:'http://localhost:8080',
    // public:'http://192.168.3.6:8080',
    disableHostCheck: true
  }
}

// module.exports = {
//   devServer: {
//     host: "0.0.0.0",  // 前端启用的地址, 0.0.0.0表示绑定该机器的所有ip地址
//     port: "8080",     // 前端启用的端口
//     disableHostCheck: true,
//     proxy: {
//       '/api': {
//         target: 'http://message.test.local',// 请求的域名 + 端口，当别人要访问时候不能是127.0.0.1
//         changeOrigin: true,// 是否跨域
//       },
//       '/static': {     //这里最好有一个 /
//         target: 'http://message.test.local',  // 后台接口域名
//         changeOrigin: true,  //是否跨域
//       }
//     }
//   },
// }