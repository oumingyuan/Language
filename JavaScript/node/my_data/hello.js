var hello={

    sayHello:function () {


        var net = require('net');


        //home
//var HOST = '192.168.0.110';

//work
        var HOST = '192.168.100.104';


        var PORT = 8888;

        var client = new net.Socket();


//请求信息
        client.connect(PORT, HOST, function () {

            console.log('connect to: ' + HOST + ' : ' + PORT);

            var request_message = 'hello world';

            client.write(request_message);

        });


//相应信息
        client.on('data', function (data) {

            console.log('DATA: ' + data);
            client.destroy();

        });

//关闭信息
        client.on('close', function () {

            console.log('connection closed');

        });





    }


};


module.exports=hello;