$(document).ready(function () {
    $('#create').click(function () {
        /*기안서*/

        $('.input').attr({
            "readonly": false,
            "disabled": false,
        });
        $('#submit').attr("style", "display:inline");
        $('#create').attr("style", "display:none");
        return false;
    });

    $('#draft').click(function () {
        /*기안서*/
        $('.view_box').children().remove();
        $('#doctype').val('draft');
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/draft.html');
        return false;
    });

    $('#voucher').click(function () {
        /*지출결의서*/
        $('.view_box').children().remove();
        $('#doctype').val('voucher');
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/voucher.html');
        return false;
    });

    $('#result').click(function () {
        /*결과보고서*/
        $('.view_box').children().remove();
        $('#doctype').val('result');
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/result.html');
        return false;
    });

    $('#meeting').click(function () {
        /*회의보고서*/
        $('.view_box').children().remove();
        $('#doctype').val('meeting');
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/meeting.html');
    });

    $('#business').click(function () {
        /*업무보고서*/
        $('.view_box').children().remove();
        $('#doctype').val('meeting');
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/business.html');
        return false;
    });
});