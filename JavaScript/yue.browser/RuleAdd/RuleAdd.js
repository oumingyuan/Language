/**
 * 
 * 1 测试增值服务编号自动生成功能
 * 
 */


$(document).ready(function() {

	$("#generateID").click(generate);

    $("#insertInformation").click(insertInformation);

    $("#insertInformationRule").click(insertInformationRule);





});



function insertInformationRule() {

    alert("insertInformationRule");

    $.post("http://localhost:8080/VASP/refresh/insertInformationRule",{},function () {

        alert("hello")

    })

}


function insertInformation() {

    alert("insert");

    $.post("http://localhost:8080/VASP/refresh/insertrule",{serverId:"ZZ20171207002"},function () {

        alert("hello")

    })

}



function generate() {

    $.post("http://localhost:8080/VASP/refresh/id",{},function (data) {

        document.getElementById("id").value = data;

    })

}




