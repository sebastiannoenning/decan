const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('UserProfile', {
    'UP.UserID': {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Users',
        key: 'UserID'
      }
    },
    Forename: {
      type: DataTypes.STRING(35),
      allowNull: false
    },
    Surname: {
      type: DataTypes.STRING(50),
      allowNull: true
    },
    DoB: {
      type: DataTypes.DATEONLY,
      allowNull: false
    },
    Photo: {
      type: DataTypes.STRING(90),
      comment: "Will direct to a filepath with the image stored.",
      allowNull: true
    },
    'UP.UserAddressID': {
      type: DataTypes.INTEGER,
      allowNull: true,
      references: {
        model: 'Address',
        key: 'AddressID'
      }
    }
  }, {
    sequelize,
    tableName: 'UserProfile',
    timestamps: false,
    indexes: [
      {
        name: "FK_User_UserProfile",
        using: "BTREE",
        fields: [
          { name: "UP.UserID" },
        ]
      },
      {
        name: "FK_Address_UserProfile",
        using: "BTREE",
        fields: [
          { name: "UP.UserAddressID" },
        ]
      },
    ]
  });
};
