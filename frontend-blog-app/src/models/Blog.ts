import User from "./User";

interface Blog {

    id: number;
    title: string;
    content: string;
    tags: string[];
    creationDate: string;
    author: User;
}

export default Blog;