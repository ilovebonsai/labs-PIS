var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) { 
    foldBtns[i].addEventListener("click", function(e) { 
        var post = e.target.parentElement;
        if (post.className == "one-post folded"){
            e.target.innerHTML = "Свернуть"; 
            post.className = "one-post";
        }
        else{
            e.target.innerHTML = "Развернуть"; 
            post.className = "one-post folded";
        }
    });
}
