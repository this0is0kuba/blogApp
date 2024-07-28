from datetime import datetime
from sqlmodel import Session
from database import engine
from models import User, Role, Blog, Comment, Category, Tag, BlogTagLink


def insert_initial_values():
    with Session(engine) as session:

        date_format = "%Y-%m-%d %H:%M:%S"

        user_john = User(
            username="john",
            email="john@wp.pl",
            disabled=False,
            password_hash="$2y$10$dmDjIJlDhPg9nqJ9gRIaPO9JprWLKzTT6BvBCmDqYtuSChdAyCNBW"
        )
        user_adam = User(
            username="adam",
            email="adam@wp.pl",
            disabled=False,
            password_hash="$2y$10$/6z1z5cVx3jxf6XG1yHJj.RligZaZATMzc.SP90c0HN1wLq1Ek4jW"
        )
        user_mary = User(
            username="mary",
            email="mary@wp.pl",
            disabled=True,
            password_hash="$2y$10$Wp.BTjTSeLj/2c.KrrpSdOiFzya2A5r2mf7cSVV/TWTgZuvzg/iKy"
        )

        role_user = Role(name="user", users=[user_mary, user_john])
        role_admin = Role(name="admin", users=[user_adam])

        category_food = Category(name="food")
        category_technology = Category(name="technology")
        category_transport = Category(name="transport")

        tag_coffee = Tag(name="coffee")
        tag_milk = Tag(name="milk")
        tag_food = Tag(name="food")
        tag_dish = Tag(name="dish")
        tag_snack = Tag(name="snack")
        tag_car = Tag(name="car")
        tag_drive = Tag(name="drive")
        tag_speed = Tag(name="speed")
        tag_plane = Tag(name="plane")
        tag_transfer = Tag(name="transfer")
        tag_people = Tag(name="people")
        tag_flight = Tag(name="flight")
        tag_transport = Tag(name="transport")

        blog_1 = Blog(
            title="Coffee snack",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime.Lorem ipsum dolor sit amet "
                    "consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam "
                    "assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. "
                    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-03-02 09:55:22", date_format),
            author=user_john,
            category=category_food
        )
        blog_2 = Blog(
            title="Best car",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-03-21 09:55:22", date_format),
            author=user_john,
            category=category_technology
        )
        blog_3 = Blog(
            title="New transport",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-04-12 09:55:22", date_format),
            author=user_adam,
            category=category_transport
        )
        blog_4 = Blog(
            title="Coffee snack",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, "
                    "adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum "
                    "similique, ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum "
                    "dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. "
                    "Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in "
                    "veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, "
                    "adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum "
                    "similique, ullam atque corrupti quasi labore voluptas in veniam, corporis maxime."
                    "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, "
                    "adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum "
                    "similique, ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum "
                    "dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. "
                    "Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in "
                    "veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, "
                    "adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum "
                    "similique, ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum "
                    "dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. "
                    "Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in "
                    "veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-04-15 09:55:22", date_format),
            author=user_john,
            category=category_food
        )
        blog_5 = Blog(
            title="Best car",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime.",
            creation_date=datetime.strptime("2024-04-29 09:55:22", date_format),
            author=user_adam,
            category=category_technology
        )
        blog_6 = Blog(
            title="New transport",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit."
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in veniam, "
                    "corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum "
                    "deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti "
                    "quasi labore voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-05-01 09:55:22", date_format),
            author=user_john,
            category=category_transport
        )
        blog_7 = Blog(
            title="Coffee snack",
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing elit. "
                    "Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit "
                    "amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi "
                    "quam assumenda cum similique, ullam atque corrupti quasi"
                    "labore voluptas in veniam, corporis maxime. Lorem ipsum dolor sit amet consectetur, adipisicing "
                    "elit. Animi laborum deserunt nostrum eum tenetur. Blanditiis modi quam assumenda cum similique, "
                    "ullam atque corrupti quasi labore voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-05-02 09:55:22", date_format),
            author=user_john,
            category=category_food
        )

        blog_tag_link_1_coffee = BlogTagLink(visible=True, blog=blog_1, tag=tag_coffee)
        blog_tag_link_1_milk = BlogTagLink(visible=True, blog=blog_1, tag=tag_milk)
        blog_tag_link_1_food = BlogTagLink(visible=True, blog=blog_1, tag=tag_food)
        blog_tag_link_1_dish = BlogTagLink(visible=True, blog=blog_1, tag=tag_dish)
        blog_tag_link_1_snack = BlogTagLink(visible=True, blog=blog_1, tag=tag_snack)

        blog_tag_link_2_car = BlogTagLink(visible=True, blog=blog_2, tag=tag_car)
        blog_tag_link_2_drive = BlogTagLink(visible=True, blog=blog_2, tag=tag_drive)
        blog_tag_link_2_speed = BlogTagLink(visible=True, blog=blog_2, tag=tag_speed)

        blog_tag_link_3_plane = BlogTagLink(visible=True, blog=blog_3, tag=tag_plane)
        blog_tag_link_3_transfer = BlogTagLink(visible=True, blog=blog_3, tag=tag_transfer)
        blog_tag_link_3_people = BlogTagLink(visible=True, blog=blog_3, tag=tag_people)
        blog_tag_link_3_flight = BlogTagLink(visible=False, blog=blog_3, tag=tag_flight)
        blog_tag_link_3_transport = BlogTagLink(visible=False, blog=blog_3, tag=tag_transport)

        blog_tag_link_4_coffee = BlogTagLink(visible=True, blog=blog_4, tag=tag_coffee)
        blog_tag_link_4_milk = BlogTagLink(visible=True, blog=blog_4, tag=tag_milk)
        blog_tag_link_4_food = BlogTagLink(visible=True, blog=blog_4, tag=tag_food)
        blog_tag_link_4_dish = BlogTagLink(visible=True, blog=blog_4, tag=tag_dish)
        blog_tag_link_4_snack = BlogTagLink(visible=True, blog=blog_4, tag=tag_snack)

        blog_tag_link_5_car = BlogTagLink(visible=True, blog=blog_5, tag=tag_car)
        blog_tag_link_5_drive = BlogTagLink(visible=False, blog=blog_5, tag=tag_drive)
        blog_tag_link_5_speed = BlogTagLink(visible=False, blog=blog_5, tag=tag_speed)

        blog_tag_link_6_plane = BlogTagLink(visible=False, blog=blog_6, tag=tag_plane)
        blog_tag_link_6_transfer = BlogTagLink(visible=False, blog=blog_6, tag=tag_transfer)
        blog_tag_link_6_people = BlogTagLink(visible=False, blog=blog_6, tag=tag_people)
        blog_tag_link_6_flight = BlogTagLink(visible=False, blog=blog_6, tag=tag_flight)
        blog_tag_link_6_transport = BlogTagLink(visible=False, blog=blog_6, tag=tag_transport)

        blog_tag_link_7_coffee = BlogTagLink(visible=False, blog=blog_7, tag=tag_coffee)
        blog_tag_link_7_milk = BlogTagLink(visible=False, blog=blog_7, tag=tag_milk)
        blog_tag_link_7_food = BlogTagLink(visible=False, blog=blog_7, tag=tag_food)
        blog_tag_link_7_dish = BlogTagLink(visible=False, blog=blog_7, tag=tag_dish)
        blog_tag_link_7_snack = BlogTagLink(visible=False, blog=blog_7, tag=tag_snack)

        comment_1 = Comment(
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit.",
            creation_date=datetime.strptime("2024-03-02 12:34:22", date_format),
            author=user_john,
            blog=blog_1
        )
        comment_2 = Comment(
            content="Animi laborum deserunt nostrum eum tenetur",
            creation_date=datetime.strptime("2024-03-02 12:34:22", date_format),
            author=user_adam,
            blog=blog_1
        )
        comment_3 = Comment(
            content="Blanditiis modi quam assumenda cum similique",
            creation_date=datetime.strptime("2024-03-02 12:34:22", date_format),
            author=user_adam,
            blog=blog_1
        )
        comment_4 = Comment(
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur. Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore "
                    "voluptas in veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-03-03 12:34:22", date_format),
            author=user_mary,
            blog=blog_1
        )
        comment_5 = Comment(
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit.",
            creation_date=datetime.strptime("2024-04-12 12:34:22", date_format),
            author=user_john,
            blog=blog_3
        )
        comment_6 = Comment(
            content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Animi laborum deserunt nostrum eum "
                    "tenetur.",
            creation_date=datetime.strptime("2024-04-15 12:34:22", date_format),
            author=user_mary,
            blog=blog_3
        )
        comment_7 = Comment(
            content="Blanditiis modi quam assumenda cum similique, ullam atque corrupti quasi labore voluptas in "
                    "veniam, corporis maxime.",
            creation_date=datetime.strptime("2024-04-16 12:34:22", date_format),
            author=user_john,
            blog=blog_3
        )
        comment_8 = Comment(
            content="Lorem ipsum dolor",
            creation_date=datetime.strptime("2024-05-12 12:34:22", date_format),
            author=user_john,
            blog=blog_3
        )

        session.add(role_admin)
        session.add(role_user)

        session.commit()


