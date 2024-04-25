$(function(){

    $('.btnLimpiar').click(function(){
        $('.txtEmail, .txtPassword').val('');
        $('.txtEmail').focus();
    })

    $('.btnEnviar').click(function(){
        if($.trim($('.txtEmail').val())=="")
        {
            alert("Falta especificar el correo");
            $('.txtEmail').focus();
        }
        else if($.trim($('.txtPassword').val())=="")
        {
            alert("Falta especificar la clave");
            $('.txtPassword').focus();
        }
        // validar que el correo tenga el formato correcto
        else
        {
            alert('Los datos enviados son: \n' + $('.txtEmail').val() + ' '
                                                + $('.txtPassword').val()
            )
        }
    })
})