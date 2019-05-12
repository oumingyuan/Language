/**
 *
 * 1 测试增值服务编号自动生成功能
 *
 */


$(document).ready(function () {

    $("#generateID").click(generate);

    $("#insertInformation").click(insertInformation);

    $("#insertInformationRule").click(insertInformationRule);


});


function insertInformationRule() {

    alert("insertInformationRule");

    $.post("http://localhost:8080/VASP/refresh/insertInformationRule", {}, function () {

        alert("hello")

    })

}


function insertInformation() {


    var param = {
        id: $("#id").val(),
        name:"lala",
        provider:"doubi",
        address:"lala",
        appoint:"gogo",
        begin:"2017-12-01",
        end:"2017-01-01",
        type:"手动"
    };


    document.getElementById("baseInfo").value = JSON.stringify(param);



    $.ajax({

        url: "http://localhost:8080/VASP/refresh/insertrule1",
        type: "post",
        dataType: "json",
        data: JSON.stringify(param),

        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },

        success: function (data) {

            alert("success");

            alert(JSON.stringify(data))

        },

        error: function (data) {

            alert("error");

            alert(JSON.stringify(data))

        }

    })

}


function generate() {


    $.ajax({


        url: 'http://localhost:8080/VASP/refresh/id',
        type: "post",
        dataType: "json",

        data: {},

        success: function (t) {

            //alert("success");


            //alert(JSON.stringify(t));

            document.getElementById("id").value = t.id;


        },

        error: function (t) {

            alert("error");

            alert(JSON.stringify(t))

        }

    });

}




