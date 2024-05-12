import User from "./User";

interface Comment {

    id: number;
    content: string;
    creationDate: string;
    blogId: number;
    author: User;
}

export default Comment;