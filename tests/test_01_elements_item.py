import pytest
import os
import sys

src_path = os.path.join(os.path.realpath("."), "src")
if src_path not in sys.path:
    sys.path.append(src_path)

from lbk_library import Dbal
from elements import Item

database = 'parts_test.db'

def close_database(dbref):
    dbref.sql_close()

@pytest.fixture
def open_database(tmpdir):
    path = tmpdir.join(database)
    dbref = Dbal()
    # valid connection
    dbref.sql_connect(path)
    return dbref

@pytest.fixture
def create_items_table(tmpdir):
    path = tmpdir.join(database)
    dbref = Dbal()
    # valid connection
    dbref.sql_connect(path)
    dbref.sql_query("DROP TABLE IF EXISTS 'items'")
    create_table = 'CREATE TABLE IF NOT EXISTS "items"' + \
                          '("record_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,' + \
                          ' "part_number" TEXT NOT NULL,' + \
                          ' "assembly" TEXT NOT NULL,' + \
                          ' "quantity" INTEGER NOT NULL,' + \
                          ' "condition" TEXT NOT NULL,' + \
                          ' "installed" INTEGER NOT NULL DEFAULT 0,' + \
                          ' "box" INTEGER DEFAULT NULL,' + \
                          ' "remarks" TEXT DEFAULT NULL)'
    dbref.sql_query(create_table)
    return dbref

# set item values from array of values
item_values = dict({'record_id': 9876,
                    'part_number': '13215',
                    'assembly': 'P',
                    'quantity': 4,
                    'condition': 'New',
                    'installed': 1,
                    'remarks': 'test',
                    'box': 5})


def test_0101_constr(open_database):
    dbref = open_database
    item = Item(dbref)
    assert isinstance(item, Item)
    close_database(dbref)

def test_0102_get_table(open_database):
    dbref = open_database
    item = Item(dbref)
    assert item.get_table() == 'items'
    close_database(dbref)

def test_0103_get_dbref(open_database):
    dbref = open_database
    item = Item(dbref)
    assert item.get_dbref() == dbref
    close_database(dbref)

def test_0104_get_set_record_id(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
#    assert item.get_record_id() == defaults['record_id']
    item._set_property('record_id', None)
    assert defaults['record_id'] == item.get_record_id()
    item._set_property('record_id', item_values['record_id'])
    assert item_values['record_id'] == item.get_record_id()
    result = item.set_record_id(None)
    assert not result['valid']
    assert result['entry'] is None
    result = item.set_record_id(-1)
    assert not result['valid']
    assert result['entry'] == -1
    result = item.set_record_id(item_values['record_id'])
    assert result['valid']
    assert result['entry'] == item_values['record_id']
    close_database(dbref)

def test_0105_get_set_part_number(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('part_number', item_values['part_number'])
    assert item_values['part_number'] == item.get_part_number()
    item._set_property('part_number', None)
    assert item.defaults['part_number'] == item.get_part_number()
    result = item.set_part_number(None)
    assert not result['valid']
    assert result['entry'] == None
    result = item.set_part_number(item_values['part_number'])
    assert result['valid']
    assert result['entry'] == item_values['part_number']
    assert result['entry'] == item.get_part_number()
    close_database(dbref)

def test_0106_get_set_assembly(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('assembly', item_values['assembly'])
    assert item_values['assembly'] == item.get_assembly()
    item._set_property('assembly', None)
    assert defaults['assembly'] == item.get_assembly()
    result = item.set_assembly(None)
    assert not result['valid']
    assert result['entry'] is None
    result = item.set_assembly(item_values['assembly'])
    assert result['valid']
    assert result['entry'] == item_values['assembly']
    assert result['entry'] == item.get_assembly()
    close_database(dbref)

def test_0107_get_set_quantity(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('quantity', item_values['quantity'])
    assert item_values['quantity'] == item.get_quantity()
    item._set_property('quantity', None)
    assert defaults['quantity'] == item.get_quantity()
    result = item.set_quantity(None)
    assert not result['valid']
    assert result['entry'] == None
    result = item.set_quantity(-1)
    assert not result['valid']
    assert result['entry'] == -1
    result = item.set_quantity(item_values['quantity'])
    assert result['valid']
    assert result['entry'] == item_values['quantity']
    assert result['entry'] == item.get_quantity()
    close_database(dbref)

def test_0108_get_set_condition(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('condition', item_values['condition'])
    assert item_values['condition'] == item.get_condition()
    item._set_property('condition', None)
    assert defaults['condition'] == item.get_condition()
    result = item.set_condition(None)
    assert not result['valid']
    assert result['entry'] is None
    result = item.set_condition(item_values['condition'])
    assert result['valid']
    assert result['entry'] == item_values['condition']
    assert result['entry'] == item.get_condition()
    close_database(dbref)

def test_0109_get_set_installed(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('installed', item_values['installed'])
    assert item_values['installed'] == item.get_installed()
    item._set_property('installed', None)
    assert defaults['installed'] == item.get_installed()
    result = item.set_installed(None)
    assert not result['valid']
    assert result['entry'] == 0
    result = item.set_installed(3)
    assert not result['valid']
    assert result['entry'] == 0
    result = item.set_installed(item_values['installed'])
    assert result['valid']
    assert result['entry'] == item_values['installed']
    assert result['entry'] == item.get_installed()
    close_database(dbref)

def test_0110_get_set_box(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('box', item_values['box'])
    assert item_values['box'] == item.get_box()
    item._set_property('box', None)
    assert defaults['box'] == item.get_box()
    result = item.set_box(None)
    assert not result['valid']
    assert result['entry'] == None
    result = item.set_box(-1)
    assert not result['valid']
    assert result['entry'] == -1
    result = item.set_box(item_values['box'])
    assert result['valid']
    assert result['entry'] == item_values['box']
    assert result['entry'] == item.get_box()
    close_database(dbref)

def test_0111_get_set_remarks(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    item._set_property('remarks', None)
    assert defaults['remarks'] == item.get_remarks()
    result = item.set_remarks(None)
    assert result['valid']
    assert result['entry'] == ''
    result = item.set_remarks(item_values['remarks'])
    assert result['valid']
    assert result['entry'] == item_values['remarks']
    assert result['entry'] == item.get_remarks()
    close_database(dbref)

def test_0112_get_properties_type(open_database):
    dbref = open_database
    item = Item(dbref)
    data = item.get_properties()
    assert isinstance(data, dict)
    close_database(dbref)

def test_0113_item_get_default_property_values(open_database):
    dbref = open_database
    item = Item(dbref)
    defaults = item.get_initial_values()
    assert item.get_remarks() == defaults['remarks']
    assert item.get_part_number() == defaults['part_number']
    assert item.get_assembly() == defaults['assembly']
    assert item.get_quantity() == defaults['quantity']
    assert item.get_condition() == defaults['condition']
    assert item.get_installed() == defaults['installed']
    assert item.get_box() == defaults['box']
    close_database(dbref)

def test_0114_set_properties_from_dict(open_database):
    # set Item from array
    dbref = open_database
    item = Item(dbref)
    item.set_properties(item_values)
    assert item_values['record_id'] == item.get_record_id()
    assert item_values['part_number'] == item.get_part_number()
    assert item_values['assembly'] == item.get_assembly()
    assert item_values['quantity'] == item.get_quantity()
    assert item_values['condition'] == item.get_condition()
    assert item_values['installed'] == item.get_installed()
    assert item_values['remarks'] == item.get_remarks()
    assert item_values['box'] == item.get_box()
    close_database(dbref)

def test_0115_item_get_properties_size(open_database):
    dbref = open_database
    item = Item(dbref)
    print(item._defaults)
    print(item.get_properties())
    assert len(item.get_properties()) == len(item_values)
    close_database(dbref)

def test_0116_item_from_dict(open_database):
    # set Part from array
    dbref = open_database
    item = Item(dbref, item_values)
    assert item_values['record_id'] == item.get_record_id()
    assert item_values['part_number'] == item.get_part_number()
    assert item_values['assembly'] == item.get_assembly()
    assert item_values['quantity'] == item.get_quantity()
    assert item_values['condition'] == item.get_condition()
    assert item_values['installed'] == item.get_installed()
    assert item_values['remarks'] == item.get_remarks()
    assert item_values['box'] == item.get_box()
    close_database(dbref)

def test_0117_item_from__partial_dict(open_database):
    dbref = open_database
    del item_values['assembly']
    item = Item(dbref, item_values)
    assert item_values['record_id'] == item.get_record_id()
    assert item_values['part_number'] == item.get_part_number()
    assert '' == item.get_assembly()
    assert item_values['quantity'] == item.get_quantity()
    assert item_values['condition'] == item.get_condition()
    assert item_values['installed'] == item.get_installed()
    assert item_values['remarks'] == item.get_remarks()
    assert item_values['box'] == item.get_box()
    close_database(dbref)

def test_0118_item_add(create_items_table):
    dbref = create_items_table
    item = Item(dbref, item_values)
    item_id = item.add()
    assert item_id == 1
    assert item_id == item.get_record_id()
    assert item_values['part_number'] == item.get_part_number()
    assert item_values['assembly'] == item.get_assembly()
    assert item_values['quantity'] == item.get_quantity()
    assert item_values['condition'] == item.get_condition()
    assert item_values['installed'] == item.get_installed()
    assert item_values['remarks'] == item.get_remarks()
    assert item_values['box'] == item.get_box()
    close_database(dbref)

def test_0119_item_read_db(create_items_table):
    dbref = create_items_table
    item = Item(dbref)
    item.set_properties(item_values)
    item_id = item.add()
    assert item_id == 1
        # read db for existing item
    item2 = Item(dbref, 1)
    assert item2.get_properties() is not None
    assert item2.get_record_id() == 1
    assert item_values['part_number'] == item2.get_part_number()
    assert item_values['assembly'] == item2.get_assembly()
    assert item_values['quantity'] == item2.get_quantity()
    assert item_values['condition'] == item2.get_condition()
    assert item_values['installed'] == item2.get_installed()
    assert item_values['remarks'] == item2.get_remarks()
    assert item_values['box'] == item2.get_box()
        # read db for non-existing item
    item3 = Item(dbref, 5)
    assert isinstance(item3.get_properties(), dict)
    assert len(item3.get_properties()) == len(item_values)
        # Try direct read thru Element
    item2.set_properties(item2.get_properties_from_db(None, None))
    assert isinstance(item2.get_properties(), dict)
    assert len(item2.get_properties()) == 0
    close_database(dbref)

def test_0120_item_update(create_items_table):
    dbref = create_items_table
    item = Item(dbref)
    item.set_properties(item_values)
    item_id = item.add()
    assert item_id == 1
    assert item_values['quantity'] == item.get_quantity()
        # update item quantity
    item.set_quantity(6)
    result = item.update()
    assert result
    assert item.get_properties() is not None
    assert item.get_record_id() == 1
    assert item_values['part_number'] == item.get_part_number()
    assert item_values['assembly'] == item.get_assembly()
    assert not item_values['quantity'] == item.get_quantity()
    assert item.get_quantity() == 6
    assert item_values['condition'] == item.get_condition()
    assert item_values['installed'] == item.get_installed()
    assert item_values['remarks'] == item.get_remarks()
    assert item_values['box'] == item.get_box()
    close_database(dbref)

def test_0121_item_delete(create_items_table):
    dbref = create_items_table
    item = Item(dbref)
    item.set_properties(item_values)
    item.add()
        #delete item
    result = item.delete()
    assert result
        #make sure it is really gone
    item = Item(dbref, 1)
    assert isinstance(item.get_properties(), dict)
    assert len(item.get_properties()) == 8
    close_database(dbref)

#end test_01_elements_item.py
