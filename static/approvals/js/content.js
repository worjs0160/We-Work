$(document).ready(function () {
    $('#new_doc').click(function () {
        /*새 문서 작성*/
        $(".approval-body").children().remove();
        $(".approval-body").load('new_doc');
        return false;
    });
});