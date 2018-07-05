import main

if __name__ == '__main__':
    # TODO: Consider moving this to tests/
    main.db.drop_all()
    main.db.create_all()
    user1 = main.UserModel(username='luke')
    main.db.session.add(user1)
    user2 = main.UserModel(username='bob')
    main.db.session.add(user2)
    main.db.session.commit()
