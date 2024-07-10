const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Tags', {
    TagID: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    TagName: {
      type: DataTypes.STRING(32),
      allowNull: false
    },
    TagDescription: {
      type: DataTypes.TEXT,
      allowNull: true
    },
    TagIcon: {
      type: DataTypes.STRING(90),
      allowNull: true
    },
    'T.CreatorUserID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Users',
        key: 'UserID'
      }
    }
  }, {
    sequelize,
    tableName: 'Tags',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "TagID" },
        ]
      },
      {
        name: "FK_User_Tag",
        using: "BTREE",
        fields: [
          { name: "T.CreatorUserID" },
        ]
      },
    ]
  });
};
