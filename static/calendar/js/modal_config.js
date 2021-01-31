$(function () {
    // 생성버튼 연결
    $("#create-event").modalForm({
        formURL: "{% url 'calendars:event_new' %}"
    });
});