import abc


class LevelLike(abc.ABC):
    def __init__(self, world, level, object_set):
        self.world = world
        self.level = level
        self.object_set_number = object_set

        self.objects = []

        self.width = 1
        self.height = 1

        self.name = "LevelLike object"

        self.object_pattern_table = None

        self.changed = False
        self.attached_to_rom = True

    @abc.abstractmethod
    def index_of(self, obj):
        pass

    @abc.abstractmethod
    def object_at(self, x, y):
        pass

    @abc.abstractmethod
    def get_object_names(self):
        pass

    @abc.abstractmethod
    def get_all_objects(self):
        pass

    @abc.abstractmethod
    def get_object(self, index):
        pass

    @abc.abstractmethod
    def remove_object(self, obj):
        pass

    @abc.abstractmethod
    def draw(self, dc, block_length, transparency):
        pass

    @abc.abstractmethod
    def to_bytes(self):
        pass

    @abc.abstractmethod
    def from_bytes(self, object_data, enemy_data):
        pass