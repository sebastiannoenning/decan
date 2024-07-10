const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Events_Tags', {
    'ET.EventID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Events',
        key: 'EventID'
      }
    },
    'ET.TagID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Tags',
        key: 'TagID'
      }
    }
  }, {
    sequelize,
    tableName: 'Events_Tags',
    timestamps: false,
    indexes: [
      {
        name: "FK_ET_Event",
        using: "BTREE",
        fields: [
          { name: "ET.EventID" },
        ]
      },
      {
        name: "FK_ET_Tags",
        using: "BTREE",
        fields: [
          { name: "ET.TagID" },
        ]
      },
    ]
  });
};
