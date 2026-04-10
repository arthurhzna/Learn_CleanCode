"""
FACTORY PATTERN
Focus: How objects are created

Problems:
- The class (UserService) still depends on the factory
- Contains selection logic (if-else)
- Still relatively tightly coupled
"""


# ======================
# 1. Interface / Base Class
# ======================
class Database:
    def connect(self):
        raise NotImplementedError


# ======================
# 2. Concrete Implementations
# ======================
class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"


class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"


# ======================
# 3. Factory
# ======================
class DatabaseFactory:
    @staticmethod
    def create(db_type: str) -> Database:
        # Factory is responsible for creating objects
        if db_type == "mysql":
            return MySQL()
        elif db_type == "postgres":
            return PostgreSQL()
        else:
            raise ValueError("Unknown database type")


# ======================
# 4. Service (uses factory)
# ======================
class UserService:
    def __init__(self, db_type: str):
        # ❌ Dependency Injection is NOT used
        # This class decides its own dependency
        self.database = DatabaseFactory.create(db_type)

    def process(self):
        return self.database.connect()


# ======================
# 5. Usage
# ======================
service = UserService("mysql")
print(service.process())

"""
CONCLUSION:
- UserService depends on DatabaseFactory
- Not flexible for testing (hard to inject mock)
- Contains selection logic in the factory (if-else)
"""


"""
DEPENDENCY INJECTION (DI)
Focus: Dependencies are provided from outside, not created internally

Advantages:
- Loose coupling
- Easy to test
- Cleaner (follows SOLID / DIP principles)
"""


# ======================
# 1. Interface / Base Class
# ======================
class Database:
    def connect(self):
        raise NotImplementedError


# ======================
# 2. Concrete Implementations
# ======================
class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"


class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"


# ======================
# 3. Service (uses DI)
# ======================
class UserService:
    def __init__(self, database: Database):
        # ✅ Dependency is injected from outside
        self.database = database

    def process(self):
        return self.database.connect()


# ======================
# 4. Usage
# ======================
db = MySQL()  # created externally
service = UserService(db)

print(service.process())

"""
CONCLUSION:
- UserService does not know the database type
- More flexible
- Can inject mocks for testing
"""

"""
COMBINATION: FACTORY + DI

This is commonly used in real-world applications:
- Factory → creates objects
- DI → injects objects into classes

Result:
- Flexible
- Clean
- Scalable
"""


# ======================
# 1. Interface
# ======================
class Database:
    def connect(self):
        raise NotImplementedError


# ======================
# 2. Implementations
# ======================
class MySQL(Database):
    def connect(self):
        return "Connected to MySQL"


class PostgreSQL(Database):
    def connect(self):
        return "Connected to PostgreSQL"


# ======================
# 3. Factory
# ======================
class DatabaseFactory:
    @staticmethod
    def create(db_type: str) -> Database:
        if db_type == "mysql":
            return MySQL()
        elif db_type == "postgres":
            return PostgreSQL()
        else:
            raise ValueError("Unknown database type")


# ======================
# 4. Service (still uses DI)
# ======================
class UserService:
    def __init__(self, database: Database):
        # ✅ Still using DI
        self.database = database

    def process(self):
        return self.database.connect()


# ======================
# 5. Composition Root (object wiring)
# ======================
# 👉 This is where objects are created and connected
db = DatabaseFactory.create("postgres")
service = UserService(db)

print(service.process())

"""
CONCLUSION:
- Factory only creates objects
- DI connects objects
- UserService remains clean (does not know how objects are created)

THIS IS BEST PRACTICE IN CLEAN ARCHITECTURE
"""
