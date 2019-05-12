var http=require("http");

var server=http.createServer(function (req,res) {


    if(req.url!=="/favicon.ico"){

        res.writeHead(200,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"http://localhost"});

        var two=require("./hello.js");


        console.log(two.sayHello());


        res.write("welcome")



    }

    res.end()



});


server.listen(1337,"localhost",function () {

    console.log("begin to listen...")

});