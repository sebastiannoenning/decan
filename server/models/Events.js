const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Events', {
    EventID: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    ETitle: {
      type: DataTypes.STRING(64),
      allowNull: false
    },
    EStart_Date: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    EEnd_Date: {
      type: DataTypes.DATEONLY,
      allowNull: true
    },
    EStart_Time: {
      type: DataTypes.TIME,
      allowNull: true
    },
    EEnd_Time: {
      type: DataTypes.TIME,
      allowNull: true
    },
    'E.CreatorUserID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Users',
        key: 'UserID'
      }
    }
  }, {
    sequelize,
    tableName: 'Events',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "EventID" },
        ]
      },
      {
        name: "FK_User_Event",
        using: "BTREE",
        fields: [
          { name: "E.CreatorUserID" },
        ]
      },
    ]
  });
};
