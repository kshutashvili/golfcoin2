(function () {
    "use strict";

    const $form = $("#login-form");
    const $submit = $form.find(".submit");

    $form.validate({
        errorPlacement: function (error, element) { },
        rules: {
            email: {
                required: true,
                email: true
            },
            password: {
                required: true
            }
        }
    });

})();