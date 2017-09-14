(function () {
    "use sctict";
    const $accordion = $(".accordion");
    const $items = $accordion.children();

    $items.each(function () {
        let $title = $(this).find(".title");
        let $parent = $title.parent();
        $title.off("click");
        $title.on("click", function (e) {
            e.preventDefault();
            $parent.toggleClass("active");
        });
    });

})();