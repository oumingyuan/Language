Page({

  //数据初始化
  data: {
    phone: '',
    password: ''
  },


  // 获取输入账号 
  phoneInput: function (e) {
    this.setData({
      phone: e.detail.value
    })
  },

  // 获取输入密码 
  passwordInput: function (e) {
    this.setData({
      password: e.detail.value
    })
  },

  // 登录 
  login: function () {
    if (this.data.phone.length == 0 || this.data.password.length == 0) {

      if (this.data.phone.length == 0) {
        wx.showToast({
          icon: 'loading',
          title: '帐号不能为空',

          duration: 2000
        })
      } else {

        if (this.data.password.length == 0) {
          wx.showToast({
            title: '密码不能为空',
            icon: 'loading',
            duration: 2000
          })
        }

      }

    } else {

      console.log("开始登录")

      // 这里修改成跳转的页面 

      wx.request({
        url: "https://www.baidu.com",
        data: "丁",
        header: {
          // "Content-Type":"application/json"
        },
        success: function (res) {
          console.log(res.data)
        },
        fail: function (err) {
          console.log(err)
        }

      })



      wx.showToast({
        title: '登录成功',
        icon: 'success',
        duration: 2000
      })



    }
  },





})
