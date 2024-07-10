var DataTypes = require("sequelize").DataTypes;
var _Address = require("./Address");
var _Events = require("./Events");
var _Events_Tags = require("./Events_Tags");
var _Events_Users = require("./Events_Users");
var _Tags = require("./Tags");
var _UserProfile = require("./UserProfile");
var _Users = require("./Users");

function initModels(sequelize) {
  var Address = _Address(sequelize, DataTypes);
  var Events = _Events(sequelize, DataTypes);
  var Events_Tags = _Events_Tags(sequelize, DataTypes);
  var Events_Users = _Events_Users(sequelize, DataTypes);
  var Tags = _Tags(sequelize, DataTypes);
  var UserProfile = _UserProfile(sequelize, DataTypes);
  var Users = _Users(sequelize, DataTypes);

  UserProfile.belongsTo(Address, { as: "UP.UserAddress", foreignKey: "UP.UserAddressID"});
  Address.hasMany(UserProfile, { as: "UserProfiles", foreignKey: "UP.UserAddressID"});
  Events_Tags.belongsTo(Events, { as: "ET.Event", foreignKey: "ET.EventID"});
  Events.hasMany(Events_Tags, { as: "Events_Tags", foreignKey: "ET.EventID"});
  Events_Users.belongsTo(Events, { as: "EU.Event", foreignKey: "EU.EventID"});
  Events.hasMany(Events_Users, { as: "Events_Users", foreignKey: "EU.EventID"});
  Events_Tags.belongsTo(Tags, { as: "ET.Tag", foreignKey: "ET.TagID"});
  Tags.hasMany(Events_Tags, { as: "Events_Tags", foreignKey: "ET.TagID"});
  Events.belongsTo(Users, { as: "E.CreatorUser", foreignKey: "E.CreatorUserID"});
  Users.hasMany(Events, { as: "Events", foreignKey: "E.CreatorUserID"});
  Events_Users.belongsTo(Users, { as: "EU.User", foreignKey: "EU.UserID"});
  Users.hasMany(Events_Users, { as: "Events_Users", foreignKey: "EU.UserID"});
  Tags.belongsTo(Users, { as: "T.CreatorUser", foreignKey: "T.CreatorUserID"});
  Users.hasMany(Tags, { as: "Tags", foreignKey: "T.CreatorUserID"});
  UserProfile.belongsTo(Users, { as: "UP.User", foreignKey: "UP.UserID"});
  Users.hasMany(UserProfile, { as: "UserProfiles", foreignKey: "UP.UserID"});

  return {
    Address,
    Events,
    Events_Tags,
    Events_Users,
    Tags,
    UserProfile,
    Users,
  };
}
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
