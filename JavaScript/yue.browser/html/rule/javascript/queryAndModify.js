/**
 * 
 */



$(document).ready(function() {
	
	radioChoose();

	getData();




	
});


function getData() {

    $.ajax({

        url : '/VASP/refresh/query',
        type : 'post',
        cache : false,
        data : new FormData($("#customerList")[0]),
        dateType : 'json',
        processData : false,
        contentType : false,
        success : function(returndata) {

            if (returndata) {
                
                alert(JSON.stringify(returndata))


            } else {

                alert('没有返回数据');

            }
        },
        error : function(returndata) {
            alert('服务端返回错误: ' + returndata);
        }


    })

}



function radioChoose() {

    $("input:radio").click(function () {

        var $radio=$(this)

        if($radio.data('waschecked')==true){

            $radio.prop('checked',false)

            $radio.data('waschecked',false)

        }else{

            $radio.prop('checked',true)

            $radio.data('waschecked',true)

        }

    })

}