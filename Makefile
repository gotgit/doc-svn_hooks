############################################################
# Customizable variables
############################################################

# TOOLS_DIR is the place where Makefile.base and other scripts present.
TOOLS_DIR := ../../tools

# XML_SRCDIR defines the place where XMLs present.
XML_SRCDIR := .

# XML_INDEX_NAME defines the main XML index page without extension.
XML_INDEX_NAME :=

# MM_SRC is FreeMind .mm filename
MM_SRC := svn_hooks.mm

# RENDER_DIR defines where rendered html, rtf, pdf present.
RENDER_DIR := .

# OUTNAME defines output HTML(no chunk), RTF, PDF, Archive(*.tar.bz2) base file name without extension.
OUTNAME := $(notdir $(shell pwd))

# Whether or not contain images/
IMAGES := $(if $(shell ls images/ 2>/dev/null), images/*,)

# $(INSTALL_DIR)/$(NAME) defines where htmls, pdf, tar.bz2 installed.
INSTALL_DIR := install

# NAME defines subdir of INSTALLed Target
NAME := $(notdir $(shell pwd))

# RENDER_OTHERS and INSTALL_OTHERS are scripts copy other necessary files to target dir.
RENDER_OTHERS :=
INSTALL_OTHERS :=

HTML_CHUNK_DIR := $(RENDER_DIR)

# Bugs of FOP may cause PDF make failed. if set to yes, not make pdf.
IGNORE_PDF_MAKE := no

# where or not create version.xml. if set to yes, generate version.xml
CREATE_VERSION_SOURCE := yes

############################################################
# Include Makefile.base
############################################################

include $(TOOLS_DIR)/Makefile.base
