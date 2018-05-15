var db;

function fnInitDB() {
    db = api.require('db');
};

var DATABASE = 'database_toutiao'

function fnOpenDatabase() {
    fnInitDB();

    db.openDatabase({
        name: DATABASE
    }, function(ret, err) {
        fnCreateFavorite();
    });
};

var FAVORITE = 'table_favorite'

function fnCreateFavorite() {
    db.executeSql({
        name: DATABASE,
        sql: 'CREATE TABLE ' + FAVORITE + '(id VARCHAR(64))'
    }, function(ret, err) {
        fnCreateFavoriteIndex();
    });
};

function fnCreateFavoriteIndex() {
    db.executeSql({
        name: DATABASE,
        sql: 'CREATE UNIQUE INDEX ' + FAVORITE + '_unique_index on ' + FAVORITE + '(id)'
    });
};

function fnGetFavoriteById(id, callback) {
    db.selectSql({
        name: DATABASE,
        sql: 'SELECT id FROM ' + FAVORITE + ' WHERE id="' + id + '"'
    }, callback);
};

function fnAddFavorite(id, callback) {
    db.executeSql({
        name: DATABASE,
        sql: 'REPLACE INTO ' + FAVORITE + '(id) VALUES("' + id + '")'
    }, callback);
};

function fnRemoveFavorite(id, callback) {
    db.executeSql({
        name: DATABASE,
        sql: 'DELETE FROM ' + FAVORITE + ' WHERE id="' + id + '"'
    }, callback);
};
