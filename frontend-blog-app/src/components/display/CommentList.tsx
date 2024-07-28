import Comment from "../../models/Comment";

function CommentList( {comments}: {comments: Comment[]} ) {
    return (
        <div>
            {
                comments.map( (comment: Comment) => (
                    <div key={comment.id} className="rounded p-2 m-2 border-bottom">
                        <h6 className="text-secondary"><b>{comment.author.username}</b></h6>
                        <p>{comment.content}</p>
                    </div>    
                ))
            }
        </div>
    );
}

export default CommentList;