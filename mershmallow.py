from fastapi import APIRouter ,File, UploadFile
from fastapi import Query
from fastapi.responses import StreamingResponse
from src.config.pymongo_get_database import *
import os
from datetime import datetime,date
import json
import pandas as pd
import io
from io import StringIO
from starlette.requests import Request
import numpy as np
# from src.endpoints.ssd_app.schemas import ItemSchema
from marshmallow import Schema, fields,ValidationError





class AddProjectRequestSchema(Schema):
    entiti_name = fields.Str(required=True)  
    loginName = fields.Str(required=True)  
    report_user =    fields.Str(required=True)  
    userId = fields.Int(required=True) 
    user = fields.List(fields.Dict(value=fields.Int(), label=fields.Str()), required=False) 

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/ssd_app/mongo_test",
    tags=["readFile"],
    responses={404: {"description": "Not found"}},
)

# Get the database using the method we defined in pymongo_test_insert file
dbname = get_database()
# collection_name = dbname["user_1_items"]


# item_1 = {
#   "_id" : "1",
#   "item_name" : "Blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340,
#   "category" : "kitchen appliance"
# }

# item_2 = {
#   "_id" : "2",
#   "item_name" : "Egg",
#   "category" : "food",
#   "quantity" : 12,
#   "price" : 36,
#   "item_description" : "brown country eggs"
# }
# collection_name.insert_one(item_1)

# db = Database()
# FIN_CEN_FINANCE = 'db_finance'

# @router.post("/")
# async def read_root(info : Request):
#      req_info = await info.json()
#      entityId = req_info['entityId']
#      cursor = db.connect('fin')
#      entityFreezeQry= "select template_type from "+FIN_CEN_FINANCE+".tbl_ril_financedata where entity_id = "+str(entityId)+" "
#      cursor.execute(entityFreezeQry)
#      freezeRes = cursor.fetchone()

#      cursor.execute("select * from "+FIN_CEN_FINANCE+".tbl_ril_financedata where entity_id = "+str(entityId)+" order by sr_no asc")
#      parentids_res = cursor.fetchall()
#      returndata = []
#      if(len(parentids_res)):
#         for row in parentids_res:
#             data = {}
#             data['userName'] = row.nameof_person_receiving
#             data['organisation'] = row.name_of_organisation
#             data['recivedPan'] = row.PAN_of_person_receiving
#             data['designation'] = row.designation_of_person_receiving
#             data['personSharing'] = row.name_of_person_sharing
#             data['panSharing'] = row.PAN_of_person_sharing
#             data['reciptDate'] = row.date_of_receipt
#             data['reciptDate_new'] = row.date_of_receipt.strftime("%d-%m-%Y")
#             data['detailsInfo'] = row.details_of_information
#             data['personEntry'] = row.name_of_person_entry
#             data['entry_date'] =  row.excel_datetime.strftime("%d-%m-%Y")
#             data['entry_time'] =   row.excel_datetime.strftime("%H:%M %p")
#             data['sr_no'] = row.sr_no
#             data['auto_id'] = row.auto_id
#             data['freese_res'] = freezeRes.template_type
            
#             returndata.append(data)
#      return {"result":returndata,'tmp_type':freezeRes.template_type}

# @router.post("/auditData")
# async def read_root(info : Request):
#      req_info = await info.json()
#      entityId = req_info['entityId']
#      cursor = db.connect('fin')

#      entityFreezeQry= "select template_type from "+FIN_CEN_FINANCE+".tbl_ril_financedata where entity_id = "+str(entityId)+" "
#      cursor.execute(entityFreezeQry)
#      entityData= cursor.fetchone()

#      cursor.execute("select * from "+FIN_CEN_FINANCE+".tbl_ril_user_audit where entity_id = "+str(entityId)+" ORDER BY sr_no asc")
#      parentids_res = cursor.fetchall()
#      returndata = []
#      if(len(parentids_res)):
#         for row in parentids_res:
#             data = {}
#             data['userName'] = row.nameof_person_receiving
#             data['active'] = 'Yes' if(row.active==1) else 'No'
#             data['db_operation'] = row.db_operation
#             data['organisation'] = row.name_of_organisation
#             data['recivedPan'] = row.PAN_of_person_receiving
#             data['designation'] = row.designation_of_person_receiving
#             data['personSharing'] = row.name_of_person_sharing
#             data['panSharing'] = row.PAN_of_person_sharing
#             data['reciptDate'] = row.date_of_receipt.strftime("%d-%m-%Y")
#             data['detailsInfo'] = row.details_of_information
#             data['created_by'] = row.created_by
#             data['modified_by'] = row.modified_by
#             data['modified_on'] = row.modified_on.strftime("%d-%m-%Y %H:%M %p") if row.modified_on!=None else "-"
#             data['entry_date'] =  row.excel_datetime.strftime("%d-%m-%Y")
#             data['entry_time'] =   row.excel_datetime.strftime("%H:%M %p")
#             data['sr_no'] = row.sr_no
            
#             returndata.append(data)
#      return {"result":returndata,"tmp_type":entityData.template_type}     


# @router.post("/singleEntry")
# async def read_root(info : Request):
#     res = 0
#     errmsg= ''
#     try:
#         req_info = await info.json()
#         userName = req_info['username']
#         organisationName = req_info['organisation']
#         recivedPan = req_info['recivedPan']
#         designation = req_info['designation']
#         panSharing = req_info['panSharing']
#         personSharing = req_info['personSharing']
#         entityId = req_info['entityId']
#         type = req_info['type']
#         loginName = req_info['loginName']
#         sr_no = req_info['sr_no']
#         reciptDate = req_info['reciptDate']
#         detailsInfo = req_info['detailsInfo']
#         autoId = req_info['auto_id']

#         cursor = db.connect('fin')
#         if(type==0):
#             typeOperation = "Insert"

#             selectSrno= " select sr_no from "+FIN_CEN_FINANCE+".tbl_ril_financedata order by sr_no desc limit 1"
#             cursor.execute(selectSrno)
#             srData = cursor.fetchone()
#             srNo = 0
#             if(srData!=None):
#                 srNo= srData.sr_no+1
#             insertEntityQry = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_financedata  SET 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving = %s,
#                     name_of_organisation   = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s, 
#                     entity_id = %s,
#                     name_of_person_entry = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     sr_no = %s,
#                     template_type=2,
#                     excel_datetime = NOW(),
#                     entry_datetime = NOW()
#                      """
#             insertEntityQryValue = (userName,recivedPan,organisationName,designation,personSharing,panSharing,entityId,loginName,reciptDate,detailsInfo,srNo)

#             insertAudit = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_user_audit  SET
#                     db_operation = %s,
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     created_by = %s,
#                     entity_id = %s,
#                     sr_no = %s,
#                     active=1,
#                     template_type=2,
#                     excel_datetime = NOW(),
#                     entry_date = NOW()
#                      """     
#             insertFinnaceVal = (typeOperation,userName,recivedPan,organisationName,designation,
#                 personSharing,panSharing,reciptDate,detailsInfo,loginName,entityId,srNo)
#         else :
#             typeOperation = "Update"
#             insertEntityQry = """ update  """+FIN_CEN_FINANCE+""".tbl_ril_financedata  SET 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving = %s,
#                     name_of_organisation   = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s, 
#                     entity_id = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     lastupdated = NOW() 
#                     where auto_id = %s
#                      """
#             insertEntityQryValue = (userName,recivedPan,organisationName,designation,personSharing,panSharing,entityId,reciptDate,detailsInfo,autoId)

#             previousAuditQry= " select * from "+FIN_CEN_FINANCE+".tbl_ril_user_audit  where sr_no = "+str(sr_no)+" order by entry_date desc limit 1"
#             cursor.execute(previousAuditQry)
#             auditData = cursor.fetchone()
#             if(auditData!=None):
#                 insertAudit = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_user_audit  SET
#                     db_operation = %s,
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     created_by = %s,
#                     entity_id = %s,
#                     sr_no=%s,
#                     excel_datetime = %s,
#                     modified_by = %s,
#                     template_type=2,
#                     entry_date = Now(),
#                     modified_on = NOW(),
#                     active=1
#                      """     
#                 insertFinnaceVal = (typeOperation,userName,recivedPan,organisationName,designation,
#                 personSharing,panSharing,reciptDate,detailsInfo,auditData.created_by,entityId,sr_no,auditData.excel_datetime,loginName)

#                 updateAuditQry = """ update  """+FIN_CEN_FINANCE+""".tbl_ril_user_audit SET 
#                 active=0
#                 where auto_id= """+str(auditData.auto_id)+"""
#                 """
            
#         try:
#             cursor.execute(insertAudit,insertFinnaceVal)
#             if(type!=0):
#                 cursor.execute(updateAuditQry)
#             cursor.execute(insertEntityQry,insertEntityQryValue)
            
#             db.commit('fin')
#             res=1
#             errmsg = typeOperation 
#         except Exception as error:
#             print(error,"dhdhj")
#             errmsg = "Something Went Wrong"
#     except Exception as Err:
#         print(Err,"dhj")
#         errmsg = "Something Went Wrong"    

#     return {"res": res,"msg":errmsg} 

# def convertDate(dateData):
#     entryDate = str(dateData).split(".") 
#     finalDate = date(int(entryDate[2]),int(entryDate[1]),int(entryDate[0]))
#     return finalDate

# def convertDateTime(dateVal,timeVal):
#     entryDate = str(dateVal).split(".")
#     timeData =  str(timeVal).split(":")
#     finalDateTime = datetime(int(entryDate[2]),int(entryDate[1]),int(entryDate[0]),int(timeData[0]),int(timeData[1]))
#     return finalDateTime



# @router.post("/upload")
# async def read_root(info:Request,file: UploadFile = File('file')):
#     entityId = info.query_params['ent']
#     templateType = info.query_params['template_type']
#     res = 0
#     errmsg = ''
#     try:
#         contents = file.file.read()
#         data = pd.read_excel(contents)
#         allData = data.to_dict('records')
#         keysList = list(data.keys())
#         # print(len(keysList),"key count")
#         if(templateType=='1' and  len(keysList) > 9 ):
#             return {"res": res,"msg":"Invalid Format"}
#         elif((templateType=='2' and  len(keysList) > 12) or (templateType=='2' and  len(keysList)==9)):
#             return {"res": res,"msg":"Invalid Format"}
#         failedCount = 0
#         cursor = db.connect('fin')
#         for row in allData:
#             try:
#                 if(templateType=='1'):
#                     srNo              = row[keysList[0]]
#                     userName          = row[keysList[1]]
#                     recivingPan       = row[keysList[2]]
#                     organsiationName  = row[keysList[3]]
#                     designationName   = row[keysList[4]]
#                     reciptDate        = convertDate(row[keysList[5]])
#                     personEntry       = row[keysList[6]]
#                     entryDateTime     = convertDateTime(row[keysList[7]],row[keysList[8]])

#                     insertQry = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_financedata  SET
#                     sr_no = %s, 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     date_of_receipt = %s,
#                     name_of_person_entry = %s,
#                     entity_id = %s,
#                     excel_datetime = %s,
#                     template_type=1,
#                     entry_datetime = NOW()
#                      """
                    
#                     insertAudit = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_user_audit  SET
#                     sr_no = %s,
#                     db_operation=%s, 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     date_of_receipt = %s,
#                     created_by = %s,
#                     entity_id = %s,
#                     excel_datetime = %s,
#                     entry_date = NOW(),
#                     template_type=1,
#                     active=1
#                     """     
#                     insertFinnaceVal = (srNo,userName,recivingPan,organsiationName,designationName,reciptDate,personEntry,entityId,entryDateTime)

#                     insertAuditVal = (srNo,'Insert',userName,recivingPan,organsiationName,designationName,
#                     reciptDate,personEntry,entityId,entryDateTime)

#                     updateQry = " update "+FIN_CEN_FINANCE+".tbl_ril_entity_master set freeze=1,last_update = NOW() where entity_id="+str(entityId)+" "
#                     cursor.execute(updateQry)
#                 else:
#                     srNo              = row[keysList[0]]
#                     userName          = row[keysList[1]]
#                     recivingPan       = row[keysList[2]]
#                     organsiationName  = row[keysList[3]]
#                     designationName   = row[keysList[4]]
#                     sharingInfoName   = "NA" if pd.isnull(row[keysList[5]])  else row[keysList[5]]
#                     sharingPan        = "NA" if pd.isnull(row[keysList[6]])  else row[keysList[6]]
#                     reciptDate        = convertDate(row[keysList[7]])
#                     infoDetails       = row[keysList[8]]
#                     personEntry       = row[keysList[9]]
#                     entryDateTime     = convertDateTime(row[keysList[10]],row[keysList[11]])

#                     insertQry = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_financedata  SET
#                     sr_no = %s, 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     name_of_person_entry = %s,
#                     entity_id = %s,
#                     excel_datetime = %s,
#                     template_type=2,
#                     entry_datetime = NOW()
#                      """
                    
#                     insertAudit = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_user_audit  SET
#                     sr_no = %s,
#                     db_operation=%s, 
# 		            nameof_person_receiving   = %s,
#                     PAN_of_person_receiving   = %s,
#                     name_of_organisation = %s,
#                     designation_of_person_receiving = %s,
#                     name_of_person_sharing = %s,
#                     PAN_of_person_sharing = %s,
#                     date_of_receipt = %s,
#                     details_of_information = %s,
#                     created_by = %s,
#                     entity_id = %s,
#                     excel_datetime = %s,
#                     template_type=2,
#                     entry_date = NOW(),
#                     active=1
#                     """     
#                     insertFinnaceVal = (srNo,userName,recivingPan,organsiationName,designationName,
#                     sharingInfoName,sharingPan,reciptDate,infoDetails,personEntry,entityId,entryDateTime)

#                     insertAuditVal = (srNo,'Insert',userName,recivingPan,organsiationName,designationName,
#                     sharingInfoName,sharingPan,reciptDate,infoDetails,personEntry,entityId,entryDateTime)

#                 try:
#                     cursor.execute(insertQry,insertFinnaceVal)
#                     cursor.execute(insertAudit,insertAuditVal)
#                 except Exception as error:
#                     print(error)
#                     failedCount +=1
#                     errmsg = "Error while Insert Query"
#             except Exception as FetchErr:
#                 print(FetchErr)
#                 errmsg = "Something Went Wrong"
#         if(failedCount==0):        
#             db.commit('fin')
#             res=1
#             errmsg = "Insert Success"         

#     except Exception as UploadErr:
#         print(UploadErr)
#         # errmsg = UploadErr
#     return {"res": res,"msg":errmsg}

# @router.post("/login")
# async def read_root(info : Request):
#     res = 0
#     errmsg= ''
#     data={}   
#     try:
#         req_info = await info.json()
#         userName = req_info['username']
#         passWord = req_info['passw']
#         cursor = db.connect('fin')
#         selectQry = """ select * from """+FIN_CEN_FINANCE+""".tbl_ril_userdetails  where username = %s and user_pass   = %s limit 1 """
#         selectVal = (userName,passWord)
#         try:
#             cursor.execute(selectQry,selectVal)
#             loginResposnse = cursor.fetchone()
#             if(loginResposnse!=None):
#                 res=1
#                 errmsg = "login Success"
#                 data['userId'] = loginResposnse.user_id
#                 data['userType'] = loginResposnse.user_type
#                 data['loginName'] = loginResposnse.user_fname + loginResposnse.user_lname
#             else:
#                 res=2
#                 errmsg="Login Failed Please Check UserName and Password"    
#         except Exception as error:
#             errmsg = error
#     except Exception as Err:
#         errmsg = Err    

#     return {"res": res,"msg":errmsg,"data":data}


# @router.post("/userList")
# async def read_root(info : Request):
#     res=0
#     userData=[]
#     try:
#         req_info = await info.json()
#         userId = req_info['userId']
#         cursor = db.connect('fin')
#         selectQry = """ select * from """+FIN_CEN_FINANCE+""".tbl_ril_userdetails  where user_id!= """+str(userId)+"""  """
#         try:
#             cursor.execute(selectQry)
#             loginResposnse = cursor.fetchall()
#             if(len(loginResposnse)):
#                 res=1
#                 for row in loginResposnse:
#                     data = {}
#                     data['value'] = row.user_id
#                     data['label'] = row.user_fname + row.user_lname
#                     userData.append(data)   
#         except Exception as error:
#             errmsg = error
#     except Exception as Err:
#         errmsg = Err    

#     return {"res":res,"data":userData}


@router.post("/createEntity")
async def read_root(info : Request):
    res = 0
    errmsg= ''
    try:
        req_info = await info.json()
        error = AddProjectRequestSchema().validate(req_info)
        if error:
            return error,422
        entityName = req_info['entiti_name']
        reportUser = req_info['report_user']
        mycol = dbname["entity"]

        # myquery  = {'entiti_name':'SDD_Q2FY23'}
        # mydoc = mycol.find(myquery)
        # for x in mydoc:
        #     print(x)
        
        for x in mycol.find():
            print(x)
        # x = mycol.find_one()
        # print(x) 
        
        # mydict = { "entiti_name": entityName, "report_user": reportUser }
        # x = mycol.insert_one(mydict)
        
        # print(x)
        # user = req_info['user']
        # json_mylist = json.dumps(user, separators=(',', ':'))
        # createdId = req_info['userId']
        # cursor = db.connect('fin')
        # selectQry =  "select entity_name from "+FIN_CEN_FINANCE+".tbl_ril_entity_master  where entity_name = '"+entityName+"'  "
        # try:
        #     cursor.execute(selectQry)
        #     entitiyResponse = cursor.fetchone()
        #     if(entitiyResponse==None):
        #         insertEntityQry = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_entity_master  SET 
		#             entity_name   = %s,
        #             entity_assign   = %s,
        #             entity_createdby = %s,
        #             report_header = %s,
        #             entry_date = NOW() """
        #         insertEntityQryValue = (entityName,json_mylist,createdId,reportUser)    
        #         try:
        #             cursor.execute(insertEntityQry,insertEntityQryValue)
        #             db.commit('fin')
        #             res=1
        #             errmsg = "Insert Success"
        #         except Exception as error:
        #             print(error)
        #             res=2
        #             errmsg = "Error while Insert Data"
        #     else:
        #         print("available")
        #         res=2
        #         errmsg="Entity Name Already Available"    
        # except Exception as error:
        #     print(error,"dhdhj")
        #     errmsg = "Something Went Wrong"
    except Exception as Err:
        print(Err,"dhj")
        errmsg = "Something Went Wrong"    

    return {"res": res,"msg":errmsg}    

# @router.post("/entity")
# async def read_root(info : Request):
#     res = 0
#     errmsg= ''
#     returndata = []
#     try:
#         req_info = await info.json()
#         userId = req_info['userId']
#         cursor = db.connect('fin')
#         #where entity_createdby = "+userId+" 
#         selectQry = " select * from "+FIN_CEN_FINANCE+".tbl_ril_entity_master order by entry_date desc"
#         try:
#             cursor.execute(selectQry)
#             entityData = cursor.fetchall()
#             if(len(entityData)):
#                 res=1
#                 for row in entityData:
#                     data= {}
#                     data['entityName'] = row.entity_name
#                     data['entityId'] = row.entity_id
#                     returndata.append(data)
#             else:
#                 res=2
#                 errmsg="No Data Available"    
#         except Exception as error:
#             errmsg = error
#     except Exception as Err:
#         errmsg = Err    

#     return {"res": res,"msg":errmsg,"data":returndata}

# @router.get("/entitylist")
# async def read_root():
#     res = 0
#     errmsg= ''
#     returndata = []
#     try:
#         cursor = db.connect('fin')
#         selectQry = " select * from "+FIN_CEN_FINANCE+".tbl_ril_entity_master order by entry_date desc"
#         try:
#             cursor.execute(selectQry)
#             entityData = cursor.fetchall()
#             if(len(entityData)):
#                 res=1
#                 for row in entityData:
#                     data= {}
#                     data['entityName'] = row.entity_name
#                     data['entityId'] = row.entity_id
#                     returndata.append(data)
#             else:
#                 res=2
#                 errmsg="No Data Available"    
#         except Exception as error:
#             errmsg = error
#     except Exception as Err:
#         errmsg = Err    

#     return {"res": res,"msg":errmsg,"data":returndata}

# @router.post("/freezeEntity")
# async def read_root(info : Request):
#     res = 0
#     errmsg= ''
#     try:
#         cursor = db.connect('fin')
#         req_info = await info.json()
#         entityId = req_info['entityId']
#         updateQry = " update "+FIN_CEN_FINANCE+".tbl_ril_entity_master set freeze=1 where entity_id="+str(entityId)+" "
#         try:
#             cursor.execute(updateQry)
#             db.commit('fin')  
#             res=1
#             errmsg = "Update Success"
#         except Exception as error:
#             print(error)
#             errmsg = "Error While Update"
#     except Exception as Err:
#         errmsg = Err    

#     return {"res": res,"msg":errmsg}

@router.get("/alltemplate")
async def read_root():
    res = 0
    errmsg= ''
    returndata = []
    try:
        cursor = db.connect('fin')
        selectTemplateQry = "select * from "+FIN_CEN_FINANCE+".tbl_ril_templates  order by autoid desc"
        try:
            cursor.execute(selectTemplateQry)
            entityData = cursor.fetchall()
            if(len(entityData)):
                res=1
                for row in entityData:
                    data= {}
                    data['id'] = row.autoid
                    data['template_name'] = row.template_name
                    returndata.append(data)
        except Exception as error:
            print(error)
            errmsg = "Error While FetchData"
    except Exception as Err:
        errmsg = Err
        print(Err)    

    return {"res": res,"msg":errmsg,"data":returndata}    

# @router.post("/insertAudit")
# async def read_root(info : Request):
#     res = 0
#     errmsg= ''
#     try:
#         req_info = await info.json()
#         operation = req_info['operation']
#         data = req_info['data']
#         jsonData = json.dumps(data, separators=(',', ':')) 
#         userId = req_info['userId']
#         userName = req_info['userName']
#         cursor = db.connect('fin')
#         insertQry = """ INSERT INTO """+FIN_CEN_FINANCE+""".tbl_ril_user_audit  SET 
# 		            db_operation   = %s,
#                     data   = %s,
#                     user_id = %s,
#                     username = %s,
#                     entry_date = NOW()
#                      """
#         insertVal = (operation,jsonData,userId,userName)
#         try:
#             cursor.execute(insertQry,insertVal)
#             db.commit('fin')
#             res=1
#             errmsg="Insert Success"    
#         except Exception as error:
#             print(error)
#             errmsg="Error While Insert Log"
#     except Exception as Err:
#         errmsg = Err    

#     return {"res": res,"msg":errmsg}            
