var answer = new Answer();

function showAnswerBody(questionId) {
    answer.setQuestionId(questionId);
    getAnswerId(questionId);
}

function Answer() {
    this.questionId = '0';
    this.answerId = '0';
    this.answerBody = 'None';
    this.answerNumber = 0;
    this.score  = "0";
}

Answer.prototype.setQuestionId = function(questionId) {
    this.questionId = questionId;
};

function setAnswerBody(data) {
    if (typeof(data.items) !== "undefined" && (data.items.length >0) ) {
        answer.answerBody = data.items[0].body;
        answer.answerNumber = data.items.length;
    }
}

function setAnswerId(data) {
    if (typeof(data.items) !== "undefined") {
        answer.answerId = data.items[0].answer_id;
        getAnswerBody(answer.answerId, setAnswerBody);
    }

}


function getAnswerBody(questionId, answerId, setAnswerBody) {
    $.getJSON("https://api.stackexchange.com/2.2/answers/" + answerId + "?order=desc&sort=activity&site=stackoverflow&filter=withbody", function(data) {
        // body...
        //setAnswerBody(data);
        if (typeof(data.items) !== "undefined") {
            answer.answerBody = data.items[0].body;
            $('#' + questionId).tooltip({
                title: answer.answerBody
            });
        }
    });
}


function getAnswerId(questionId, setAnswerId) {
    var jsonfile = $.getJSON("https://api.stackexchange.com/2.2/questions/" + questionId + "/answers?order=desc&sort=votes&site=stackoverflow", function(data) {
        if (typeof(data.items) !== "undefined") {
            answer.answerId = data.items[0].answer_id;
            answer.score = data.items[0].score;
            $("#" + questionId).html($("#" + questionId).html() + "The most upvoted Answer: " + answer.score); 
            getAnswerBody(questionId, answer.answerId, setAnswerBody);
        }
    });
}


// Attach a submit handler to the form
$(function() {

    var time = 0;
    var url = "/search";
    var $inputTitle = $("#inputTitle");
    var $titlelist = $("#titlelist");
    var $listitems = $(".list-group-item");
    var $postTitle = $("#postTitle");
    var len = 0;

    var findLen = function() {
        var title = $inputTitle.val();
        title = title.replace(/\s{2,}/g, ' ');
        var len = title.split(' ').length;
        return len;
    };
    $postTitle.on('input', function() {
        var newlen = $inputTitle.val().length;
        change = Math.abs(newlen - len);
        if (change > 5 && findLen() > 4) {
            len = newlen;
            change = 0;
            $postTitle.trigger("submit");
        }
    });


    $postTitle.submit(function(event) {

        // Stop form from submitting normally
        event.preventDefault();
        var title = $inputTitle.val();
        // var newTitle = title;
        $titlelist.empty();
        var inputTitle = {
            'inputTitle': title
        }
        var posting = $.post(url, inputTitle, function(data) {
            var questions = JSON.parse(data);
            for (var i = 0; i < questions.length; i++) {
                var title = questions[i]['Title'];
                var questionLink = "http://stackoverflow.com/questions/" + questions[i]['Id'];
                var tooltipId = questions[i]['Id'];
                var question = '<a  href="' + questionLink + '" class="list-group-item  itemMargin" data-toggle="tooltip" data-placement="right" data-html="true" id="' + tooltipId + '"><h4 class="list-group-item-heading" id="list-group-item-heading" style="text-align: left;">' + title + "</h4>]";
                $(question).appendTo("#titlelist");
                showAnswerBody(tooltipId);
                $('#' + tooltipId).hover(function (){
                    $(this).toggleClass('active');
            });

          }
        });

    });



});








