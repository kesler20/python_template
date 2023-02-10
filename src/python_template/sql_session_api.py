from typing import Any


class SQLSessionAPI:
    """The SQLSessionAPI allows to implement CRUD operations on the tables of an SQL database. 
    This is dove via SQLAlchemy tables which are the ORMs in python.
    """

    def __init__(self, db: Any, app : Any) -> None:
        with app.app_context():
            db.create_all()
            self.db = db
            self.session = db.session

    def write_value(self, new_row: Any) -> None:
        """write_value this method will add a row to the given table. i.e.

        ## Example
        ```python
        new_row = User(name='Alice', age=30)
        session = SQLSessionAPI()
        session.write_value(new_row)
        ```

        Parameters
        ---

        new_row Any
            this is the instance of the table class that we want to insert
            i.e. new_user = User(name='Alice')

        Returns
        ---
        result: None
        """
        # Insert a new row into the table
        self.session.add(new_row)
        self.session.commit()

    def update_value(self, class_table: Any, key: str, value: str, **kwargs: Any):
        print(class_table)
        self.session.query(class_table).filter_by(
            **kwargs).update({key: value})
        self.session.commit()

    def read_value(self, class_table: Any, **kwargs: Any) -> Any:
        """read_value this will read a specific value (row) from the given table. 

        # Example
        ```python
        session = SQLSessionAPI()
        session.read_value(User,name="Mark")
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User
        **kargs tuple
            this is the key value pair that we want to use for our query i.e.
            name='Paul'

        Returns
        ---
        result: tuple
            this will return all the records which meet the given conditions, i.e.
            if we are looking for name='Paul' it will return all the rows with the name 'Paul'
        """
        return self.session.query(class_table).filter_by(**kwargs).all()

    def read_all_values(self, class_table: Any) -> Any:
        """read_all_values this method will read all the values from the SQL table

        # Example
        ```python
        sesion = SQLSessionAPI()
        session.read_all_values(User)
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User

        Returns
        ---
        result: Any
        """
        # Query for all rows in the table
        return self.session.query(class_table).all()

    def delete_value(self, class_table: Any, **kwargs: Any) -> None:
        """delete_value this method can be used to delete a specific value on the table or all the values which meet a specific condition. 
        the row can be identified with a key value pair.

        ## Example
        ```python
        session = SQLSessionAPI()
        session.delete_value(User,name="Paula")
        ```

        Parameters
        ---

        class_table type
            this is the name of the class of the table i.e. User
        **kargs tuple
            this is the key value pair that we want to use for our query i.e.
            name='Paul', this will mean that we wabnt to delete all the users 
            named Paul

        Returns
        ---
        result: None
        """
        # Delete a row from the table
        rows_to_delete = self.session.query(
            class_table).filter_by(**kwargs).all()
        for row_to_delete in rows_to_delete:
            self.session.delete(row_to_delete)
        self.session.commit()
