// var dislikeCountShow, likeCountShow;

// function like_disable_fun(id, likes, dislikes) {
//     likes = parseInt(likes);
//     dislikes = parseInt(dislikes);
//     const like_count = 1;
//     const dislike_count = 0;
//     likeCountShow = document.getElementById('likecount' + id);
//     dislikeCountShow = document.getElementById('dislikecount' + id);
//     likeCountShow.innerHTML = "total like" + (likes +like_count);
//     dislikeCountShow.innerHTML = "total dislike" + (dislikes +dislike_count);
//     document.getElementById('likeBtn' + id).disabled = true;
//     document.getElementById('dislikeBtn' + id).disabled = false; 
//     update_likes(likes + like_count); 
// }
// function dislike_disable_fun(id, likes, dislikes) {
//     likes = parseInt(likes)
//     dislikes = parseInt(dislikes)
//     const like_count = 0;
//     const dislike_count = 1;
//     dislikeCountShow = document.getElementById('dislikecount' + id);
//     likeCountShow = document.getElementById('likecount' + id);
//     dislikeCountShow.innerHTML = "total dislike" + (dislikes + dislike_count);
//     likeCountShow.innerHTML = "total like" + (likes +like_count);
//     document.getElementById('likeBtn' + id).disabled = false;
//     document.getElementById('dislikeBtn' + id).disabled = true;
//     update_dislikes(dislikes + dislike_count);
// }

// function update_likes(counter) {
//       $.ajax({
//         url: 'update_likes',
//         data: {'counter': counter},
//         type: 'POST'
//       }).done(function(response){
//         console.log(response);
//       });
//     }
//     window.onblur = onchange;

// function update_dislikes(counter) {
//       $.ajax({
//         url: 'update_dislikes',
//         data: {'csrfmiddlewaretoken':"{{ csrf_token }}",
//             'counter': counter},
//         type: 'POST'
//       }).done(function(response){
//         console.log(response);
//       });
//     window.onblur = onchange;
// }
$(document).ready(function(event){
    $(document).on('click', '#like', function(event){
        event.preventDefault();
        var pk = $(this).attr('value');
        $.ajax({
            type: 'POST',
            url: '{% url "likepost" %}',
            data: {
                'id': pk,
            },
            datatype: 'json',
            // success: function(response){
            //     $('#like-section').html(response['form'])

            // },
            // error: function(rs, e){
            //     console.log(rs.responseText);
            // },
        });
    });
});