import Category from "./Category";
import User from "./User";

export interface Blog {

    id: number;
    title: string;
    content: string;
    tags: string[];
    creationDate: string;
    author: User;
    category: Category,
    authorId: number,
    categoryId: number
}