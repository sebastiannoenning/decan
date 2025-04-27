pass
"""
class EBody(QWidget):
    # Provides JSON Parsing of the Attributes column & constructs the internal body to be placed in Body & Dynamic 
    #   generation of internal body widgets
    sizeChanged = Signal()
    attributesChanged = Signal()

    def __init__(self, parent, Attributes: QByteArray = None):
        super().__init__(parent)
        self._Ui = Ui_event_body()
        self._Ui.setupUi(self)

        self._Attributes = Attributes
        self._Json          : Dict[str, QJsonValue] = {}

        # Experimental internal data list for pulling key associated with object, to provide ease of use on moving or changing the values inside.
        self._Items         : Dict[str, Union[EToDo, EDescription]] = {}

    # Getters for _Json attributes
    def returnEventType(self): return self._Json['info']['event_type']
    def returnObjectIndex(self): return self._Json['info']['object_index']
    
    def _updateChecked(self, key: str, checked: bool):
        self._Json['objects'][key]['EBool'] = checked
        self._Attributes = QJsonDocument(self._Json).toJson(QJsonDocument.JsonFormat.Compact)
    
    def _updateJson(self):
        try: self.checkJDoc(QJsonDocument.fromJson(self._Attributes))
        except Exception as e: print(f"_updateJson()->{e}")

        new_Json = (QJsonDocument.fromJson(self._Attributes)).object()
            
        if (new_Json == self._Json): return
        elif self._Json is not None: self.reformatUi(n_Json=new_Json)
        else: self.generateUi(n_Json = new_Json)
    
    def generateUi(self, n_Json: Dict[str, QJsonValue]):
        self._Json = n_Json
        objects: Dict[str, QJsonValue] = self._Json.get('objects')
        for key, val in objects.items():

            component_type, index = str(key).rsplit('_', 1)

            if  (component_type == 'EDescription'):
                txt:  str                       = str(val)

                widget = EDescription(self, key)
                widget.setObjectName(key)
                widget.setText(txt)
                widget.adjustSize()
                
            elif(component_type == 'EToDo'):
                n_val:  Dict[str, QJsonValue]   = val
                checked, txt                    = bool(n_val.get('EBool')), str(n_val.get('EDescription'))

                widget = EToDo(self, key)
                widget.setObjectName(key)
                widget.setText(txt)
                widget.adjustSize()
                widget.setChecked(checked)

                widget._Ui.checkbox.checkStateChanged.connect(lambda: self._updateChecked(key)) # Updating _Attributes will call a connection to the DB via the dataWidgetMapper
            
            self._Ui.container.addWidget(widget)
            
            self.setMaximumHeight(self._Ui.container.sizeHint().height())

    def reformatUi(self, n_Json: Dict[str, QJsonValue]):
        for key, val in n_Json.get('objects',{}).items():
            component_type, index = str(key).rsplit('_', 1)

            # If a key exists in self._Json
            if key in self._Json.get('objects',{}).keys():

                # Only run if the pre-existing ui object is mismatched w/ its value
                if (self._Json.get('objects',{}).get(key) != val):
                
                    if  (component_type == 'EDescription'): 
                        widget: EDescription            = self._Ui.container.findChild(EDescription, key)
                        n_val: str                      = val.toObject().toString()

                        if ((widget.text()) != n_val):          widget.setText(str(n_val))

                    elif(component_type == 'EToDo'):        
                        widget: EToDo                   = self._Ui.container.findChild(EToDo, key)
                        n_val:  Dict[str, QJsonValue]   = val.toObject()
                        val_bool, val_label             = bool(n_val.get('EBool').toBool()), str(n_val.get('EDescription').toString())

                        if (widget.isChecked() != val_bool):    widget.setChecked(val_bool)
                        if (widget.text() != val_label):        widget.setText(val_label)
                
                # Otherwise, pass & don't update
                else: pass
            
            # If a key does not already exist in self._Json
            else:
                if  (component_type == 'EDescription'):
                    txt:  str                       = str(val.toString())

                    widget = EDescription(self, key)
                    widget.setObjectName(key)
                    widget.setText(txt)
                    widget.adjustSize()

                elif(component_type == 'EToDo'):
                    n_val:  Dict[str, QJsonValue]   = val.toObject()
                    checked, txt                    = bool(n_val.get('EBool').toBool()), str(n_val.get('EDescription').toString())

                    widget = EToDo(self, key)
                    widget.setObjectName(key)
                    widget.setText(txt)
                    widget.adjustSize()
                    widget.setChecked(checked)

                    widget._Ui.checkbox.checkStateChanged.connect(lambda: self._updateChecked(key)) # Updating _Attributes will call a connection to the DB via the dataWidgetMapper
                
                # Attempt to match index with another object, if it exists
                for o_key in self._Json.get('objects',{}).keys():
                    o_component_type, o_index = str(o_key).rsplit('_', 1)
                    if (index == o_index):  # Previous index holder for former; note it down
                        if (component_type == 'EDescription'): deleted_widget: EDescription    = self._Ui.container.findChild(EDescription, key)
                        if (component_type == 'EToDo'):        deleted_widget: EToDo           = self._Ui.container.findChild(EToDo, key)
                
                index = (int(index) - 1)
                other_widget = self._Ui.container.itemAt(index).widget()
                if  (deleted_widget is not None): 
                    self._Ui.container.replaceWidget(deleted_widget, widget)
                    deleted_widget.deleteLater()
                elif(other_widget is not None):
                    o_c, o_i = str(other_widget.objectName()).split('_',1)
                    o_i = (int(o_i) - 1)
                    if      (o_i > index): 
                        self._Ui.container.insertWidget(index, widget)
                    elif    (o_i < index):
                        self._Ui.container.insertWidget(index, widget)
                else:
                    self._Ui.container.addWidget(widget)
        
        self._Json['objects'] = n_Json['objects']
        self._Json['info'] = n_Json['info']

    def checkJDoc(self, t_Doc: QJsonDocument):
        if t_Doc.isNull(): raise Exception("validateJDoc error: QJsonDocument Null")
        t_Json = t_Doc.object()
        if not isinstance(t_Json, dict): raise Exception("validateJDoc error: Unpacked object not dict:",type(t_Json))
        return True  
    def checkJsonStructure(self, t_Json: Dict[str, QJsonValue]):
        # Checks the Json Structure of a passed dict & checks its conformity against the expected structure; otherwise formats it
        def formatTabInfo(info_Json: Dict[str, QJsonValue] = []):
            # Formats an info tab
            object_index, event_type = info_Json.get('object_index').toInt(), info_Json.get('event_type').toInt()
            if (object_index is None): info_Json.update({'object_index',0)
            if (event_type is None): info_Json.update({'event_type',EventType.Complex.value)

            return info_Json
               
        def formatTabObject(objects_Json: Dict[str, QJsonValue] = []):
            # Formats an objects tab
            def formatEToDo(p_Json: Dict[str, QJsonValue]):
                # Remove non whitelisted keys, and if values don't pre-exist generate them
                EToDo: Dict[str, QJsonValue] = self.removeNonWhiteListedKeys(p_Json, ['EBool','ETaskDescription'])
                EBool, ETaskDescription = EToDo.get('EBool').toBool(), p_Json.get('ETaskDescription').toString()
                if (EBool is None): EToDo.update({{'EBool':False})
                if (ETaskDescription is None): EToDo.update({{'ETaskDescription':'Task'})
                return EToDo
            def formatEDescription(p_Json: Dict[str, QJsonValue]):
                # Search if any nested values/dictionary portions may have it stored, otherwise return default value 
                EDescription: str = self._jSearchKey(p_Json, 'EDescription')
                if (EDescription is None): EDescription = ''
                return EDescription

            # Convert Json Dict into a sorted list
            objects_ordered: List[Tuple[str, QJsonValue]] = sorted(
                objects_Json.items(), 
                key=lambda item: int(item[0].rsplit('_', 1)[1])
                )

            exp_index = 0 # Starting/expected index

            n_objects_Json = objects_Json.copy()
            n_objects_Json.clear()

            for key, value in objects_ordered:
                obj_type, index = key.rsplit('_', 1) # Remove split & parse index number

                exp_index += 1
                cur_index = int(index)
                
                if (cur_index != exp_index): key = f'{obj_type}_{exp_index}'

                if obj_type == 'EDescription':
                    if isinstance(value, str): pass
                    elif isinstance(value, dict): value = formatEDescription(value)
                    else: value = ''
                if obj_type == 'EToDo' :
                    value: Dict[str, QJsonValue] = formatEToDo(value)

                n_objects_Json.update({{key:value})

            return n_objects_Json

        # Extract info & objects
        tab_Info: Dict[str, QJsonValue] = formatTabInfo(t_Json.get('info').toObject())
        tab_Objects: Dict[str, QJsonValue] = t_Json.get('objects').toObject()

        # Should be fine, but adds a layer of precaution pre-reading it
        Index: int = tab_Info.get('object_index').toInt()
        if tab_Objects is not None:
            # First ensure the object branch is clear of any invalid keys
            tab_Objects = self.removeAllBlackListedKeys(tab_Objects,['object_index','event_type','info','objects'])

            # Set object_index to correct value
            if (len(tab_Objects)) == Index:         # if len(tab_Objects) == Index: 
                if Index == 0: tab_Objects = None                           # if (Index == 0) and (len(tab_Objects) == 0): Clear tab_Objects
                else: pass                                                  # if (Index == len(tab_Objects)) and (Index > 0): No action necessary          
            else:                                   # if len(tab_Objects) != Index:
                if bool(tab_Objects): Index, tab_Objects = 0, None          # if (tab_Objects.isEmpty()) and (Index != 0): Clear tab_Objects and set Index to 0
                else: Index = len(tab_Objects)                              # if (len(tab_Objects) > 0) and (len(tab_Objects) != Index): Set Index to length of tab_Objects

            if (Index != 0): tab_Objects = formatTabObject(tab_Objects)
            
            if (Index != tab_Info.get('object_index')): tab_Info.update({{'object_index':Index})
        
        n_Json: Dict[str, QJsonValue] = []
        n_Json.update({{'info':tab_Info})
        if (tab_Objects is not None): 
            tab_Objects = formatTabObject(tab_Objects)
            n_Json.update({{'objects':tab_Objects})
        
        return n_Json

    def removeAllBlackListedKeys(self, p_Json: Dict[str, QJsonValue], 
                                 bl_Keys: List[str]):
        # Recursively searches for a blacklisted key in a nested dictionary structure & removes it
        n_Json = p_Json.copy()

        for key in bl_Keys:
            self._jDeleteKey(n_Json, key)
        
        return n_Json   
    def removeNonWhiteListedKeys(self, p_Json: Dict[str, QJsonValue],
                                 wl_Keys: List[str]):
        # Looks for non-whitelisted keys in a regular/flat dictionary & removes them 
        n_Json = p_Json.copy()

        invalid_keys: List[str] = []
        for key, value in n_Json.items():
            passed = False
            for wl_key in wl_Keys:
                if key == wl_key:
                    passed = True
            if not passed: invalid_keys.append(key)
        
        for inv_key in invalid_keys: n_Json.pop(inv_key)

        return n_Json
                
    def _jCheckKeysExist(self, root_dict: dict, fields: List[str]):
        for field in fields:
            found = self._jSearchKeyBool(root_dict, field)
            if not found: raise Exception(f'checkFields() error: jsonSearch() could not find "{field}"')
        return True
    def _jSearchKeyBool(self, s_dict: Dict[str, QJsonValue], field: str):
        # Wrapper that converts into bool
        value = self._jSearchKey(s_dict, field)
        if (value is not None): return True
        else: return False
    def _jSearchKey(self, s_dict: Dict[str, QJsonValue], field: str):
        # Recursive json search function that searches for a field in a dictionary & if found the value associated
        if field in s_dict: return s_dict[field]
        for key, val in s_dict.items():             
            if isinstance(val, dict):
                value = self._jSearchKey(val, field)
                if (value is not None): return value

    def _jDeleteKey(self, s_dict: Dict[str, QJsonValue], field: str):
        # Recursive definitive json search which culminates in deleting a key (& any repeats) from a dictionary
        #   Be careful: Deleted keys have no way to be recovered.
        #
        #   Use as following:
        #       'yourDict: Dict[str, QJsonValue] = self._jDeleteKey(yourDict, key)'
        if field in s_dict: 
            s_dict.pop(field)
            return s_dict
        for key, val in s_dict.items():
            if isinstance(val, dict):
                value = self._jDeleteKey(val, field)
                if isinstance(value, dict): # If any dictionary was deleted, it'll return as type dictionary
                    if (len(value) == 0):   # If the key didn't contain any other information,
                        s_dict.pop(key)     # delete the key
                    else:
                        s_dict[key] = value # Otherwise, update the dictionary
        return s_dict
    def _jCountKeyRepeats(self, s_dict: Dict[str, QJsonValue], field: str):
        # Recursive json search that checks for repeated keys
        number: int = 0 
        if field in s_dict: number += 1
        for key, val in s_dict.items():
            if isinstance(val, dict):
                num = self._jCountKeyRepeats(val, field)
                if isinstance(num, int): number+=num
        return number

    @Property(QByteArray)
    def Attributes(self): return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes: QByteArray):
        if (self._Attributes != Attributes):
            self._Attributes = Attributes
            if (QJsonDocument.fromJson(self._Attributes).object() != self._Json): self._updateJson()
            self.attributesChanged.emit()

        pass
        CREATE ALGORITHM = MERGE VIEW `EU_FilteredEvents` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `Events_Users` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    )
WHERE
    `EU`.`EU_UserID` = 1;

DROP TABLE IF EXISTS `EU_layer1_FilteredEvents`;
DROP TABLE IF EXISTS `EU_layer2_FilteredEvents`;
    
CREATE ALGORITHM = MERGE VIEW `EU_layer1_FilteredEvents` AS SELECT
    `Events_Users`.`EU_EventID` AS `EU_EventID`
FROM
    `Events_Users`
WHERE
    `Events_Users`.`EU_UserID` = 3;

CREATE ALGORITHM = MERGE VIEW `EU_layer2_FilteredEvents` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `EU_layer1_FilteredEvents` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    );

ALTER VIEW `EU_layer1_FilteredEvents` AS 
SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = 2;

SELECT * FROM `Users` WHERE `UserID` = 1


SELECT `EU_UserID` FROM `Events_Users` WHERE `EU_UserID` = 3 
INTERSECT
SELECT * FROM `EU_layer1_FilteredEvents`

--
-- Triggers `Events`
--
DELIMITER $$
CREATE TRIGGER `AUTO_Event_Initial_JSON_Format` BEFORE INSERT ON `Events` FOR EACH ROW BEGIN
	DECLARE object_index INT DEFAULT 0;
	DECLARE event_type INT DEFAULT 0;
	DECLARE info JSON DEFAULT JSON_OBJECT('object_index', 0, 'event_type', 0);
    	DECLARE objects JSON DEFAULT JSON_OBJECT();
		-- If none specified, generate a default value --
		IF (NEW.EAttributes IS Null OR NEW.Eattributes ='') THEN
        		SET NEW.EAttributes = JSON_OBJECT("info", info);
		ELSE
            -- Extract any $.info attributes & set to local variables -- 
          	IF JSON_EXTRACT(NEW.EAttributes, "$.info") IS Null THEN
              	IF (JSON_EXISTS(NEW.EAttributes, "$.object_index") IS NOT Null) THEN
					SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$.object_index") AS UNSIGNED);
                    SET info = JSON_SET(info, "object_index", object_index);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.object_index");
				END IF;
				IF (JSON_EXISTS(NEW.EAttributes, "$.event_type") IS NOT Null) THEN
					SET event_type = JSON_VALUE(NEW.EAttributes, "$.event_type");
                    SET info = JSON_SET(info, "event_type", event_type);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.event_type");
				END IF;
            -- Otherwise, if info provided --
          	ELSE
            	-- Local store --
            	SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$info.object_index") AS UNSIGNED);
            	SET event_type = JSON_VALUE(NEW.EAttributes, "$info.event_type");
                
                SET info = JSON_EXTRACT(NEW.EAttributes, "$.info");
                SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.info");
            END IF;
            -- After that if-else execution, any info values should be safely contained in $.info with their individual values in object_index & event_type -- 
        	-- Check then for existence of keys in absence of objects -- 
        	IF JSON_EXTRACT(NEW.EAttributes, "$.objects") IS Null THEN
                -- Post processing existing keys, check if the attributes leftover are still equal to 0
                IF JSON_LENGTH(JSON_KEYS(NEW.EAttributes)) > 0 THEN
                	SET objects = NEW.EAttributes;
                END IF;
            -- However, if $.objects is there -- 
		ELSE
                -- Extract objects as standalone JSON_OBJECT --
                SET objects = JSON_EXTRACT(NEW.EAttributes, "$.objects");
            END IF;
                
            -- Quickly update the object_index if there's a mismatch between the predicted lengths --     
            IF (JSON_LENGTH(JSON_KEYS(objects)) != object_index) THEN
                -- Take the count of objects & update the index --
                SET object_index = CAST(JSON_LENGTH(JSON_KEYS(objects)) AS UNSIGNED)
                SET info = JSON_SET(info, "object_index", object_index);
            END IF;
            
            -- If object_index is still 0, only add info tab --
            IF (object_index == 0) THEN
                SET NEW.EAttributes = JSON_OBJECT(
                 	'info', info
                );
            ELSE
                SET NEW.EAttributes = JSON_OBJECT(
                  	'info', info,
                    'objects', objects
                ); 
            END IF;
        END IF;
	END
$$
DELIMITER ;
        
def new_dump():
    SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `decan`
--

DROP TABLE IF EXISTS `Events_Tags`;
DROP TABLE IF EXISTS `Events_Users`;
DROP TABLE IF EXISTS `Events`;
DROP VIEW IF EXISTS `EU_FilteredEvents`;
DROP VIEW IF EXISTS `EU_Events_edit`;
DROP VIEW IF EXISTS `EU_Events_access`;

-- --------------------------------------------------------

--
-- Table structure for table `Events`
--

CREATE TABLE `decan`.`Events` 
(`EventID` INT(6) NOT NULL AUTO_INCREMENT ,
 `ETitle` VARCHAR(64) NOT NULL ,
 `EStart` DATETIME NOT NULL ,
 `EEnd` DATETIME NOT NULL CHECK (`EEnd` >= `EStart`) , 
 `EAttributes` JSON NULL ,
 `E_CreatorUserID` INT(3) NOT NULL ,
 `E_LocationID` INT(10) NULL ,
CONSTRAINT `PK_Event` PRIMARY KEY (`EventID`) ,
CONSTRAINT `FK_User_Event` 
FOREIGN KEY (`E_CreatorUserID`) REFERENCES `Users`(`UserID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
FOREIGN KEY (`E_LocationID`) REFERENCES `Address`(`AddressID`) 
ON DELETE SET NULL ON UPDATE NO ACTION )
ENGINE = InnoDB;

CREATE TABLE `decan`.`Events_Users` 
(`EU_EventID` INT(6) NOT NULL ,
 `EU_UserID` INT(3) NOT NULL ,
CONSTRAINT `PK_EU` PRIMARY KEY (`EU_EventID`,`EU_UserID`) ,
CONSTRAINT `FK_EU_Event` 
FOREIGN KEY (`EU_EventID`) REFERENCES `Events`(`EventID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
CONSTRAINT `FK_EU_User` 
FOREIGN KEY (`EU_UserID`) REFERENCES `Users`(`UserID`) 
ON DELETE CASCADE ON UPDATE NO ACTION )
ENGINE = InnoDB;

CREATE TABLE `decan`.`Events_Tags` 
(`ET_EventID` INT(6) NOT NULL ,
 `ET_TagID` INT(3) NOT NULL ,
CONSTRAINT `PK_ET` PRIMARY KEY (`ET_EventID`,`ET_TagID`) ,
CONSTRAINT `FK_ET_Event` 
FOREIGN KEY (`ET_EventID`) REFERENCES `Events`(`EventID`) 
ON DELETE CASCADE ON UPDATE NO ACTION ,
CONSTRAINT `FK_ET_Tags` 
FOREIGN KEY (`ET_TagID`) REFERENCES `Tags`(`TagID`) 
ON DELETE CASCADE ON UPDATE NO ACTION )
ENGINE = InnoDB;

--
-- Triggers `Events`
--
DELIMITER $$
CREATE TRIGGER `AUTO_Event_Initial_JSON_Format` BEFORE INSERT ON `Events` FOR EACH ROW BEGIN
	DECLARE object_index INT DEFAULT 0;
	DECLARE event_type INT DEFAULT 0;
	DECLARE info JSON DEFAULT JSON_OBJECT('object_index', 0, 'event_type', 0);
	DECLARE objects JSON DEFAULT JSON_OBJECT();
	-- If none specified, generate a default value --
		IF (NEW.EAttributes IS Null OR NEW.Eattributes ='') THEN
        		SET NEW.EAttributes = JSON_OBJECT("info", info);
		ELSE
            -- Extract any $.info attributes & set to local variables -- 
          		IF JSON_EXTRACT(NEW.EAttributes, "$.info") IS Null THEN
          			IF (JSON_EXISTS(NEW.EAttributes, "$.object_index") IS NOT Null) THEN
					SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$.object_index") AS UNSIGNED);
					SET info = JSON_SET(info, "object_index", object_index);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.object_index");
				END IF;
				IF (JSON_EXISTS(NEW.EAttributes, "$.event_type") IS NOT Null) THEN
					SET event_type = JSON_VALUE(NEW.EAttributes, "$.event_type");
					SET info = JSON_SET(info, "event_type", event_type);
					SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.event_type");
				END IF;
            			-- Otherwise, if info provided --
            		ELSE
            			-- Local store --
            			SET object_index = CAST(JSON_VALUE(NEW.EAttributes, "$info.object_index") AS UNSIGNED);
            			SET event_type = JSON_VALUE(NEW.EAttributes, "$info.event_type");
            			
            			SET info = JSON_EXTRACT(NEW.EAttributes, "$.info");
            			SET NEW.EAttributes = JSON_REMOVE(NEW.EAttributes, "$.info");
            		END IF;
            		
            		-- After that if-else execution, any info values should be safely contained in $.info with their individual values in object_index & event_type -- 
            		-- Check then for existence of keys in absence of objects -- 
            		IF JSON_EXTRACT(NEW.EAttributes, "$.objects") IS Null THEN
            			-- Post processing existing keys, check if the attributes leftover are still equal to 0
            			IF JSON_LENGTH(JSON_KEYS(NEW.EAttributes)) > 0 THEN
            				SET objects = NEW.EAttributes;
            			END IF;
            		-- However, if $.objects is there --
            		ELSE
            			-- Extract objects as standalone JSON_OBJECT --
            			SET objects = JSON_EXTRACT(NEW.EAttributes, "$.objects");
            		END IF;
            		
            		-- Quickly update the object_index if there's a mismatch between the predicted lengths --
            		IF (JSON_LENGTH(JSON_KEYS(objects)) != object_index) THEN
            			-- Take the count of objects & update the index --
            			SET object_index = CAST(JSON_LENGTH(JSON_KEYS(objects)) AS UNSIGNED);
            			SET info = JSON_SET(info, "object_index", object_index);
            		END IF;
            		
            		-- If object_index is still 0, only add info tab --
            		IF object_index = 0 THEN
            			SET NEW.EAttributes = JSON_OBJECT(
            				'info', info
            			);
            		ELSE
            			SET NEW.EAttributes = JSON_OBJECT(
            				'info', info,
            				'objects', objects
            			); 
            		END IF;
            	END IF;
	END
$$
DELIMITER ;

--
-- Dumping data for table `Events`
--

INSERT INTO `Events` (`EventID`, `ETitle`, `EStart`, `EEnd`, `EAttributes`, `E_CreatorUserID`, `E_LocationID`) VALUES
(3, 'Date with Danielle', '2024-04-05 20:00:00', '2024-04-05 20:25:00', '{\"object_index\": 0}', 2, NULL),
(4, 'Halloween Party', '2024-10-23 23:00:00', '2024-10-24 02:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Bring a costume that shares your initial!\"}', 1, NULL),
(5, 'Shopping', '2024-10-15 20:00:00', '2024-10-15 20:25:00', '{\"object_index\": 0}', 2, NULL),
(6, 'James Trip', '2024-10-26 23:00:00', '2024-10-27 00:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Going fishing with James!\"}', 3, NULL),
(7, 'Christmas', '2024-12-25 00:00:00', '2024-12-25 23:59:00', '{\"object_index\": 1, \"EDescription_1\": \"Santa Clause is coming to town!\"}', 1, NULL),
(8, 'Christmas Shopping', '2024-12-25 20:00:00', '2024-12-25 20:25:00', '{\"EToDo_1\":{\"EBool\":false,\"ETaskDescription\":\"Buy Gerald Shoes\"},\"object_index\":1}', 1, NULL),
(9, 'Gaming session', '2024-11-04 23:00:00', '2024-11-05 02:00:00', '{\"object_index\": 0}', 2, NULL),
(10, 'Fun times at beach', '2024-10-12 23:00:00', '2024-10-13 02:00:00', '{\"object_index\": 1, \"EDescription_1\": \"Bring a costume that shares your initial!\"}', 2, NULL),
(11, 'Shopping at Walmart', '2024-10-24 19:00:00', '2024-10-24 20:00:00', '{\"EDescription_3\":\"Check if there is any baby carriers as well\",\"EToDo_1\":{\"EBool\":false,\"ETaskDescription\":\"Buy eggs\"},\"EToDo_2\":{\"EBool\":false,\"ETaskDescription\":\"Buy milk\"},\"object_index\":3}', 3, NULL),
(17, 'Dentist', '2025-02-09 00:00:00', '2025-02-10 00:00:00', '{\"object_index\": 0}', 3, NULL);
    
CREATE ALGORITHM = MERGE VIEW `EU_Events_edit` AS SELECT
    `Events_Users`.`EU_EventID` AS `EU_EventID`
FROM
    `Events_Users`
WHERE
    `Events_Users`.`EU_UserID` = 3;

CREATE ALGORITHM = MERGE VIEW `EU_Events_access` AS SELECT
    `E`.*
FROM
    (
        `Events` `E`
    JOIN `EU_Events_edit` `EU` ON
        (`E`.`EventID` = `EU`.`EU_EventID`)
    );

ALTER VIEW `EU_Events_edit` AS 
SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = 2;

SELECT * FROM `Events` WHERE 
(
    (
        (`EStart_Date` <= '2024-04-30' AND COALESCE(`EEnd_Date`,`EStart_Date`) >= '2023-03-00')
    ) OR (
        (`EStart_Date` <= '2025-05-30' AND COALESCE(`EEnd_Date`,`EStart_Date`) >= '2024-11-00')
    )
)
AND `E_CreatorUserID` = 2

--
-- AUTO_INCREMENT for table `Events`
--
ALTER TABLE `Events`
  MODIFY `EventID` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Dumping data for table `Events_Users`
--

INSERT INTO `Events_Users` (`EU_EventID`, `EU_UserID`) VALUES
(3, 1),
(3, 3),
(4, 3),
(5, 1),
(6, 1),
(6, 2),
(8, 2),
(10, 3);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

#1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'ALTER TABLE `Events`
  MODIFY `EventID` int(6) NOT NULL AUTO_INCREMENT, AUTO...' at line 14
        
class CEventUserModel(QSqlTableModel): #Access model for view in database
    def __init__(self, /, parent = ..., db = ...):
        super().__init__(parent, db)
        test_en = True
        self._user_id = 1

        self.setTable('EU_layer2_FilteredEvents')
        self.select()

        # Query ran once to check current user in table
        self.pullUser = QSqlQuery("SHOW CREATE VIEW `EU_layer1_FilteredEvents`")
        self.currentUser()

        self.userValidate = QSqlQuery() #Query for validating the _user_id passed to the 
        self.userValidate.prepare("SELECT * FROM `Users` WHERE `UserID` = :user ;")
        self.userChange = QSqlQuery() #Query for changing the view's current user
        self.userChange.prepare("ALTER VIEW `EU_layer1_FilteredEvents` AS SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user ;")
        
        self.intersectingRowCheck = QSqlQuery() #Query for checking common rows between the predicted & current dataset
        self.intersectingRowCheck.prepare(
                                  SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                  INTERSECT
                                  SELECT * FROM `EU_layer1_FilteredEvents`)
        
        self.intersectingRowCount = QSqlQuery() #Query for number of checking common rows
        self.intersectingRowCount.prepare(
                                    SELECT COUNT(*) AS intersection_count
                                    FROM (
                                        SELECT `EU_EventID` FROM `Events_Users` WHERE `EU_UserID` = :user 
                                        INTERSECT
                                        SELECT * FROM `EU_layer1_FilteredEvents`
                                    ) AS intersecting_rows)
        
    def currentUser(self, test_en=True):
        self.pullUser = sqlFuncs.execnext(self.pullUser)                                                           # Error messages to be passed to terminal
        uid_check, msg = re.search('`EU_UserID`\s*=\s*(\d+)',self.pullUser.value(1)),                                       'N/A'
        if (uid_check): self._user_id, msg = uid_check.group(1),                                                            'Successfully managed to'
        else:           self._user_id, msg = int(sqlFuncs.execnext(QSqlQuery("SELECT `UserID` FROM `Users` LIMIT 1")).value(0)),     'Failed to'
        # Above code checks if a match was found in the view's initial query; if not, it defaults to another user. 
        if (test_en): print(f"###EUModel {msg} extract ID from view\nCurrent UserID: ",self._user_id)
        if ((msg) == 'Failed to'): self.changeUser(uid=self._user_id)
    
    def changeUser(self, uid: int, test_en=True):
        if (uid == self._user_id): return #Exit early if _user_id already matches the current
        else:
            # Validate userID
            cur_id = self._user_id
            self.userValidate.bindValue(":user", uid)
            self.userValidate = sqlFuncs.execnext(self.userValidate)
            if not (self.userValidate.isValid()):
                if (test_en): print(f"###EUModel Validate Error: {self.userValidate.lastError()}")
                return #Exit early if _user_id does not exist
            else: self._user_id = uid 
            # Change view Query
            self.userChange.bindValue(":user", uid)
            self.userChange.exec()
            self.select()
            self.intersectingRowCount.bindValue(':user', cur_id)
            same_rows = sqlFuncs.execnext(self.intersectingRowCount).value(0)
            if (test_en): print('###EUModel: User changed\n#### (Overall) Matching:New Rows: (',self.rowCount(),') ',same_rows,':',self.rowCount()-same_rows)"""