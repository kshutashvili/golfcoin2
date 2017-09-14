(function () {
    "use strict";

    const $form = $("#donation-form");
    const $submit = $form.find(".submit");

    $form.validate({
        errorPlacement: function (error, element) { },
        ignore: '',
        rules: {
            payment_method: {
                required: true
            },
            address: {
                required: true
            },
            e20_wallet: {
                required: true
            },
            transaction_address: {
                required: true
            },
        }
    });

})();