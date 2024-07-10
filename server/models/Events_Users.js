const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Events_Users', {
    'EU.EventID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Events',
        key: 'EventID'
      }
    },
    'EU.UserID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Users',
        key: 'UserID'
      }
    }
  }, {
    sequelize,
    tableName: 'Events_Users',
    timestamps: false,
    indexes: [
      {
        name: "FK_EU_Event",
        using: "BTREE",
        fields: [
          { name: "EU.EventID" },
        ]
      },
      {
        name: "FK_EU_User",
        using: "BTREE",
        fields: [
          { name: "EU.UserID" },
        ]
      },
    ]
  });
};
