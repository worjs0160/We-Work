$(document).ready(function () {

    $('#draft').click(function () {
        /*기안서*/
        $('.view_box').children().remove();
        $('.view_box').load('doc_format/draft.html');
        return false;
    });

    $('#voucher').click(function () {
        /*지출결의서*/
        $('.view_box').children().remove();
        $('.view_box').load('doc_format/voucher.html');
        return false;
    });

    $('#result').click(function () {
        /*결과보고서*/
        $('.view_box').children().remove();
        $('.view_box').load('doc_format/result.html');
        return false;
    });

    $('#meeting').click(function () {
        /*회의보고서*/
        $('.view_box').children().remove();
        $('.view_box').load('doc_format/meeting.html');
        return false;
    });

    $('#business').click(function () {
        /*업무보고서*/
        $('.view_box').children().remove();
        $('.view_box').load('doc_format/business.html');
        return false;
    });
});