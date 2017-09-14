(function () {
    "use strict";

    const $form = $("#signup-form");
    const $submit = $form.find(".submit");

    $form.validate({
        errorPlacement: function (error, element) { },
        rules: {
            name: {
                required: true
            },
            surname: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            password: {
                required: true
            },
            confirm_password: {
                required: true,
                equalTo: "#password"
            }
        }
    });

})();