(function () {
    "use strict";

    const $form = $("#password-recovery-form");
    const $submit = $form.find(".submit");

    $form.validate({
        errorPlacement: function (error, element) { },
        rules: {
            email: {
                required: true,
                email: true
            }
        }
    });

})();