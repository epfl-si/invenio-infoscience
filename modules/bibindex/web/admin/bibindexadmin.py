## This file is part of Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Invenio BibIndex Administrator Interface."""

__revision__ = "$Id$"

__lastupdated__ = """$Date$"""

import invenio.bibindexadminlib as bic
from invenio.webpage import page, create_error_box
from invenio.config import CFG_SITE_URL, CFG_SITE_LANG, CFG_SITE_NAME
from invenio.dbquery import Error
from invenio.webuser import getUid, page_not_authorized

def deletetag(req, fldID, ln=CFG_SITE_LANG, tagID=-1, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_deletetag(fldID=fldID,
                                               ln=ln,
                                               tagID=tagID,
                                               callback=callback,
                                               confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def addtag(req, fldID, ln=CFG_SITE_LANG, value=['',-1], name='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_addtag(fldID=fldID,
                                            ln=ln,
                                            value=value,
                                            name=name,
                                            callback=callback,
                                            confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyfieldtags(req, fldID, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_modifyfieldtags(fldID=fldID,
                                                   ln=ln,
                                                   callback=callback,
                                                   confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def addindexfield(req, idxID, ln=CFG_SITE_LANG, fldID='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_addindexfield(idxID=idxID,
                                            ln=ln,
                                            fldID=fldID,
                                            callback=callback,
                                            confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyindexfields(req, idxID, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_modifyindexfields(idxID=idxID,
                                                   ln=ln,
                                                   callback=callback,
                                                   confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def showdetailsfieldtag(req, fldID, tagID, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_showdetailsfieldtag(fldID=fldID,
                                                         tagID=tagID,
                                                         ln=ln,
                                                         callback=callback,
                                                         confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def showdetailsfield(req, fldID, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_showdetailsfield(fldID=fldID,
                                                      ln=ln,
                                                      callback=callback,
                                                      confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyfield(req, fldID, ln=CFG_SITE_LANG, code='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_modifyfield(fldID=fldID,
                                                 ln=ln,
                                                 code=code,
                                                 callback=callback,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyindex(req, idxID, ln=CFG_SITE_LANG, idxNAME='', idxDESC='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_modifyindex(idxID=idxID,
                                                 ln=ln,
                                                 idxNAME=idxNAME,
                                                 idxDESC=idxDESC,
                                                 callback=callback,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyindexstemming(req, idxID, ln=CFG_SITE_LANG, idxSTEM='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_modifyindexstemming(idxID=idxID,
                                                 ln=ln,
                                                 idxSTEM=idxSTEM,
                                                 callback=callback,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)


def modifytag(req, fldID, tagID, ln=CFG_SITE_LANG, name='', value='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_modifytag(fldID=fldID,
                                               tagID=tagID,
                                               ln=ln,
                                               name=name,
                                               value=value,
                                               callback=callback,
                                               confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def deletefield(req, fldID, ln=CFG_SITE_LANG, confirm=0):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_deletefield(fldID=fldID,
                                                 ln=ln,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def deleteindex(req, idxID, ln=CFG_SITE_LANG, confirm=0):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_deleteindex(idxID=idxID,
                                                 ln=ln,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def showfieldoverview(req, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage logical fields",
                    body=bic.perform_showfieldoverview(ln=ln,
                                                 callback=callback,
                                                 confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def editfields(req, ln=CFG_SITE_LANG, callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage logical fields",
                    body=bic.perform_editfields(ln=ln,
                                                callback=callback,
                                                confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def editfield(req, fldID, ln=CFG_SITE_LANG, mtype='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_editfield(fldID=fldID,
                                               ln=ln,
                                               mtype=mtype,
                                               callback=callback,
                                               confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def editindex(req, idxID, ln=CFG_SITE_LANG, mtype='', callback='yes', confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)


    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_editindex(idxID=idxID,
                                               ln=ln,
                                               mtype=mtype,
                                               callback=callback,
                                               confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyindextranslations(req, idxID, ln=CFG_SITE_LANG, sel_type='', trans = [], confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_modifyindextranslations(idxID=idxID,
                                                        ln=ln,
                                                        sel_type=sel_type,
                                                        trans=trans,
                                                        confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def modifyfieldtranslations(req, fldID, ln=CFG_SITE_LANG, sel_type='', trans = [], confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_modifyfieldtranslations(fldID=fldID,
                                                        ln=ln,
                                                        sel_type=sel_type,
                                                        trans=trans,
                                                        confirm=confirm),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def addfield(req, ln=CFG_SITE_LANG, fldNAME='', code='', callback="yes", confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage logical fields",
                    body=bic.perform_addfield(ln=ln,
                                              fldNAME=fldNAME,
                                              code=code,
                                              callback=callback,
                                              confirm=confirm),
                    uid=uid,
                    language=ln,
                    navtrail = navtrail_previous_links,
                    req=req,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def addindex(req, ln=CFG_SITE_LANG, idxNAME='', callback="yes", confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage Indexes",
                    body=bic.perform_addindex(ln=ln,
                                              idxNAME=idxNAME,
                                              callback=callback,
                                              confirm=confirm),
                    uid=uid,
                    language=ln,
                    navtrail = navtrail_previous_links,
                    req=req,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def switchtagscore(req, fldID, id_1, id_2, ln=CFG_SITE_LANG):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_switchtagscore(fldID=fldID,
                                                    id_1=id_1,
                                                    id_2=id_2,
                                                    ln=ln),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def removeindexfield(req, idxID, fldID, ln=CFG_SITE_LANG, callback="yes", confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/index">Manage Indexes</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Index",
                    body=bic.perform_removeindexfield(idxID=idxID,
                                                    fldID=fldID,
                                                    ln=ln,
                                                    callback=callback,
                                                    confirm=confirm),
                    uid=uid,
                    language=ln,
                    navtrail = navtrail_previous_links,
                    req=req,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def removefieldtag(req, fldID, tagID, ln=CFG_SITE_LANG, callback="yes", confirm=-1):
    navtrail_previous_links = bic.getnavtrail() + """&gt; <a class="navtrail" href="%s/admin/bibindex/bibindexadmin.py/field">Manage logical fields</a> """ % (CFG_SITE_URL)

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Edit Logical Field",
                    body=bic.perform_removefieldtag(fldID=fldID,
                                                    tagID=tagID,
                                                    ln=ln,
                                                    callback=callback,
                                                    confirm=confirm),
                    uid=uid,
                    language=ln,
                    navtrail = navtrail_previous_links,
                    req=req,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)


def index(req, ln=CFG_SITE_LANG, mtype='', content=''):
    navtrail_previous_links = bic.getnavtrail()

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage Indexes",
                    body=bic.perform_index(ln=ln,
                                           mtype=mtype,
                                           content=content),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def field(req, ln=CFG_SITE_LANG, mtype='', content=''):
    navtrail_previous_links = bic.getnavtrail()

    try:
        uid = getUid(req)
    except Error, e:
        return error_page(req)

    auth = bic.check_user(req,'cfgbibindex')
    if not auth[0]:
        return page(title="Manage logical fields",
                    body=bic.perform_field(ln=ln,
                                           mtype=mtype,
                                           content=content),
                    uid=uid,
                    language=ln,
                    req=req,
                    navtrail = navtrail_previous_links,
                    lastupdated=__lastupdated__)
    else:
        return page_not_authorized(req=req, text=auth[1], navtrail=navtrail_previous_links)

def error_page(req, ln=CFG_SITE_LANG, verbose=1):
    return page(title="Internal Error",
                body = create_error_box(req, verbose=verbose, ln=ln),
                description="%s - Internal Error" % CFG_SITE_NAME,
                keywords="%s, Internal Error" % CFG_SITE_NAME,
                language=ln,
                req=req)
