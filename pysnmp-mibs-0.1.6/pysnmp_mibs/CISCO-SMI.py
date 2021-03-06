#
# PySNMP MIB module CISCO-SMI (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/CISCO-SMI
# Produced by pysmi-0.0.7 at Sun Feb 14 00:06:19 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( ObjectIdentifier, OctetString, Integer, ) = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
( ModuleCompliance, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
( iso, Gauge32, Counter32, ObjectIdentity, Counter64, enterprises, Unsigned32, Bits, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter32", "ObjectIdentity", "Counter64", "enterprises", "Unsigned32", "Bits", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9)).setRevisions(("2012-08-29 00:00", "2009-02-03 00:00", "2002-03-21 00:00", "2001-05-22 00:00", "2000-11-01 22:46", "2000-01-11 00:00", "1997-04-09 00:00", "1995-05-16 00:00", "1994-04-26 20:00",))
if mibBuilder.loadTexts: cisco.setLastUpdated('201208290000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cisco.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: cisco.setDescription('The Structure of Management Information for the\n        Cisco enterprise.')
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
if mibBuilder.loadTexts: ciscoProducts.setDescription('ciscoProducts is the root OBJECT IDENTIFIER from\n        which sysObjectID values are assigned.  Actual\n        values are defined in CISCO-PRODUCTS-MIB.')
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
if mibBuilder.loadTexts: local.setDescription('Subtree beneath which pre-10.2 MIBS were built.')
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
if mibBuilder.loadTexts: temporary.setDescription('Subtree beneath which pre-10.2 experiments were\n        placed.')
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
if mibBuilder.loadTexts: pakmon.setDescription('reserved for pakmon')
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
if mibBuilder.loadTexts: workgroup.setDescription('subtree reserved for use by the Workgroup Business Unit')
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
if mibBuilder.loadTexts: otherEnterprises.setDescription('otherEnterprises provides a root object identifier\n        from which mibs produced by other companies may be\n        placed.  mibs produced by other enterprises are\n        typicially implemented with the object identifiers\n        as defined in the mib, but if the mib is deemed to\n        be uncontrolled, we may reroot the mib at this\n        subtree in order to have a controlled version.')
ciscoSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1))
if mibBuilder.loadTexts: ciscoSB.setDescription('ciscoSB provides root Object Identifier for Management\n        Information Base for products of Cisco Small Business.\n        This includes products rebranded from linksys aquisition.\n        MIB numbers under this root are managed and controlled\n        by ciscosb_mib@cisco.com.')
ciscoSMB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 2))
if mibBuilder.loadTexts: ciscoSMB.setDescription('ciscoSMB provides root Object Identifier for Management\n        Information Base for products of Cisco built for Small and \n        Medium Business market.The MIB numbers under this root are \n        managed and controlled by ciscosmb_mib@cisco.com')
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
if mibBuilder.loadTexts: ciscoAgentCapability.setDescription('ciscoAgentCapability provides a root object identifier\n        from which AGENT-CAPABILITIES values may be assigned.')
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
if mibBuilder.loadTexts: ciscoConfig.setDescription('ciscoConfig is the main subtree for configuration mibs.')
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
if mibBuilder.loadTexts: ciscoMgmt.setDescription('ciscoMgmt is the main subtree for new mib development.')
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
if mibBuilder.loadTexts: ciscoExperiment.setDescription('ciscoExperiment provides a root object identifier\n        from which experimental mibs may be temporarily\n        based.  mibs are typicially based here if they\n        fall in one of two categories\n        1) are IETF work-in-process mibs which have not\n        been assigned a permanent object identifier by\n        the IANA.\n        2) are cisco work-in-process which has not been\n        assigned a permanent object identifier by the\n        cisco assigned number authority, typicially because\n        the mib is not ready for deployment.\n\n        NOTE WELL:  support for mibs in the ciscoExperiment\n        subtree will be deleted when a permanent object\n        identifier assignment is made.')
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
if mibBuilder.loadTexts: ciscoAdmin.setDescription('ciscoAdmin is reserved for administratively assigned\n        OBJECT IDENTIFIERS, i.e. those not associated with MIB\n        objects')
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
if mibBuilder.loadTexts: ciscoModules.setDescription('ciscoModules provides a root object identifier\n        from which MODULE-IDENTITY values may be assigned.')
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
if mibBuilder.loadTexts: lightstream.setDescription('subtree reserved for use by Lightstream')
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
if mibBuilder.loadTexts: ciscoworks.setDescription('ciscoworks provides a root object identifier beneath\n        which mibs applicable to the CiscoWorks family of network\n        management products are defined.')
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
if mibBuilder.loadTexts: newport.setDescription('subtree reserved for use by the former Newport Systems\n        Solutions, now a portion of the Access Business Unit.')
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
if mibBuilder.loadTexts: ciscoPartnerProducts.setDescription('ciscoPartnerProducts is the root OBJECT IDENTIFIER from\n        which partner sysObjectID values may be assigned. Such \n        sysObjectID values are composed of the ciscoPartnerProducts\n        prefix, followed by a single identifier that is unique for \n        each partner, followed by the value of sysObjectID of the\n        Cisco product from which partner product is derived.  Note\n        that the chassisPartner MIB object defines the value of the\n        identifier assigned to each partner.')
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
if mibBuilder.loadTexts: ciscoPolicy.setDescription('ciscoPolicy is the root of the Cisco-assigned OID\n        subtree for use with Policy Management.')
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
if mibBuilder.loadTexts: ciscoPIB.setDescription('ciscoPIB is the root of the Cisco-assigned OID\n        subtree for assignment to PIB (Policy Information\n        Base) modules.')
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
if mibBuilder.loadTexts: ciscoPolicyAuto.setDescription('ciscoPolicyAuto is the root of the Cisco-assigned\n        OID subtree for OIDs which are automatically assigned\n        for use in Policy Management.')
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
if mibBuilder.loadTexts: ciscoPibToMib.setDescription("ciscoPibToMib is the root of the Cisco-assigned\n        OID subtree for MIBs which are algorithmically\n        generated/translated from Cisco PIBs with OIDs\n        assigned under the ciscoPIB subtree.\n        These generated MIBs allow management\n        entities (other the current Policy Server) to\n        read the downloaded policy.  By convention, for PIB\n        'ciscoPIB.x', the generated MIB shall have the\n        name 'ciscoPibToMib.x'.")
ciscoDomains = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19))
if mibBuilder.loadTexts: ciscoDomains.setDescription('ciscoDomains provides a root object identifier from which\n        different transport mapping values may be assigned.')
ciscoCIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20))
if mibBuilder.loadTexts: ciscoCIB.setDescription('ciscoCIB is the root of the Cisco-assigned OID subtree for\n        assignment to MIB modules describing managed objects that\n        part of the CPE automatic configuration framework.')
ciscoCibMmiGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 1))
if mibBuilder.loadTexts: ciscoCibMmiGroup.setDescription('ciscoCibMmiGroup is the root of the Cisco-assigned OID\n        subtree for assignment to MIB modules describing managed\n        objects supporting the Modem Management Interface (MMI),\n        the interface that facilitates CPE automatic configuration.')
ciscoCibProvGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 2))
if mibBuilder.loadTexts: ciscoCibProvGroup.setDescription('ciscoCibStoreGroup is the root of the Cisco-assigned OID\n        subtree for assignment to MIB modules describing managed\n        objects contributing to the Configuration Information Base\n        (CIB).')
ciscoPKI = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 21))
if mibBuilder.loadTexts: ciscoPKI.setDescription('ciscoPKI is the root of cisco-assigned OID subtree for PKI\n        Certificate Policies and Certificate Extensions.')
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
if mibBuilder.loadTexts: ciscoProxy.setDescription('ciscoProxy OBJECT IDENTIFIERS are used to uniquely name\n        party mib records created to proxy for SNMPv1.')
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
if mibBuilder.loadTexts: ciscoRptrGroupObjectID.setDescription('ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to\n        uniquely identify groups of repeater ports for use by the\n        SNMP-REPEATER-MIB (RFC 1516) rptrGroupObjectID object.')
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
if mibBuilder.loadTexts: ciscoUnknownRptrGroup.setDescription('The identity of an unknown repeater port group.')
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
if mibBuilder.loadTexts: cisco2505RptrGroup.setDescription('The authoritative identity of the Cisco 2505 repeater\n        port group.')
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
if mibBuilder.loadTexts: cisco2507RptrGroup.setDescription('The authoritative identity of the Cisco 2507 repeater\n        port group.')
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
if mibBuilder.loadTexts: cisco2516RptrGroup.setDescription('The authoritative identity of the Cisco 2516 repeater\n        port group.')
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
if mibBuilder.loadTexts: ciscoWsx5020RptrGroup.setDescription('The authoritative identity of the wsx5020 repeater\n        port group.')
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
if mibBuilder.loadTexts: ciscoChipSets.setDescription('Numerous media-specific MIBS have an object, defined as\n        an OBJECT IDENTIFIER, which is the identity of the chipset\n        realizing the interface.  Cisco-specific chipsets have their \n        OBJECT IDENTIFIERS assigned under this subtree.')
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
if mibBuilder.loadTexts: ciscoChipSetSaint1.setDescription('The identity of the Rev 1 SAINT ethernet chipset\n        manufactured for cisco by LSI Logic.')
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
if mibBuilder.loadTexts: ciscoChipSetSaint2.setDescription('The identity of the Rev 2 SAINT ethernet chipset\n        manufactured for cisco by LSI Logic.')
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
if mibBuilder.loadTexts: ciscoChipSetSaint3.setDescription('The identity of the Rev 3 SAINT ethernet chipset\n        manufactured for cisco by Plessey.')
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
if mibBuilder.loadTexts: ciscoChipSetSaint4.setDescription('The identity of the Rev 4 SAINT ethernet chipset\n        manufactured for cisco by Mitsubishi.')
ciscoTDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 19, 99999))
ciscoTDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 1))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv4.setDescription('The UDP over IPv4 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv4.')
ciscoTDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 2))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv6.setDescription('The UDP over IPv6 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv6 for global IPv6\n        addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
ciscoTDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 3))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv4.setDescription('The TCP over IPv4 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv4.')
ciscoTDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 4))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv6.setDescription('The TCP over IPv6 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv6 for global IPv6\n        addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
ciscoTDomainLocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 5))
if mibBuilder.loadTexts: ciscoTDomainLocal.setDescription('The Posix Local IPC transport domain. The corresponding\n        transport address is of type CiscoTAddressLocal.  The Posix\n        Local IPC transport domain incorporates the well known UNIX\n        domain sockets.')
ciscoTDomainClns = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 6))
if mibBuilder.loadTexts: ciscoTDomainClns.setDescription('The CLNS transport domain.  The corresponding transport\n        address is of type CiscoTAddressOSI.')
ciscoTDomainCons = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 7))
if mibBuilder.loadTexts: ciscoTDomainCons.setDescription('The CONS transport domain.  The corresponding transport\n        address is of type CiscoTAddressOSI.')
ciscoTDomainDdp = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 8))
if mibBuilder.loadTexts: ciscoTDomainDdp.setDescription('The DDP transport domain.  The corresponding transport\n        address is of type CiscoTAddressNBP.')
ciscoTDomainIpx = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 9))
if mibBuilder.loadTexts: ciscoTDomainIpx.setDescription('The IPX transport domain.  The corresponding transport\n        address is of type CiscoTAddressIPX.')
ciscoTDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 10))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv4.setDescription('The SCTP over IPv4 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv4.')
ciscoTDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 11))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv6.setDescription('The SCTP over IPv6 transport domain.  The corresponding\n        transport address is of type CiscoTAddressIPv6 for global IPv6\n        addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
mibBuilder.exportSymbols("CISCO-SMI", cisco2505RptrGroup=cisco2505RptrGroup, ciscoTDomainCons=ciscoTDomainCons, ciscoTDomainSctpIpv6=ciscoTDomainSctpIpv6, ciscoTDomainTcpIpv6=ciscoTDomainTcpIpv6, PYSNMP_MODULE_ID=cisco, cisco2516RptrGroup=cisco2516RptrGroup, ciscoAdmin=ciscoAdmin, local=local, ciscoUnknownRptrGroup=ciscoUnknownRptrGroup, ciscoTDomainUdpIpv6=ciscoTDomainUdpIpv6, ciscoModules=ciscoModules, cisco2507RptrGroup=cisco2507RptrGroup, ciscoProxy=ciscoProxy, ciscoChipSets=ciscoChipSets, ciscoAgentCapability=ciscoAgentCapability, ciscoTDomainDdp=ciscoTDomainDdp, ciscoPKI=ciscoPKI, ciscoMgmt=ciscoMgmt, ciscoCIB=ciscoCIB, ciscoPibToMib=ciscoPibToMib, ciscoTDomains=ciscoTDomains, ciscoExperiment=ciscoExperiment, ciscoPolicyAuto=ciscoPolicyAuto, ciscoPartyProxy=ciscoPartyProxy, ciscoConfig=ciscoConfig, ciscoChipSetSaint1=ciscoChipSetSaint1, newport=newport, ciscoRptrGroupObjectID=ciscoRptrGroupObjectID, ciscoChipSetSaint2=ciscoChipSetSaint2, pakmon=pakmon, ciscoCibProvGroup=ciscoCibProvGroup, ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup, lightstream=lightstream, temporary=temporary, ciscoTDomainSctpIpv4=ciscoTDomainSctpIpv4, ciscoChipSetSaint4=ciscoChipSetSaint4, ciscoTDomainIpx=ciscoTDomainIpx, ciscoTDomainTcpIpv4=ciscoTDomainTcpIpv4, workgroup=workgroup, ciscoworks=ciscoworks, ciscoCibMmiGroup=ciscoCibMmiGroup, ciscoDomains=ciscoDomains, ciscoChipSetSaint3=ciscoChipSetSaint3, ciscoTDomainUdpIpv4=ciscoTDomainUdpIpv4, ciscoPIB=ciscoPIB, ciscoTDomainLocal=ciscoTDomainLocal, ciscoContextProxy=ciscoContextProxy, otherEnterprises=otherEnterprises, ciscoSB=ciscoSB, ciscoPartnerProducts=ciscoPartnerProducts, ciscoSMB=ciscoSMB, ciscoTDomainClns=ciscoTDomainClns, cisco=cisco, ciscoPolicy=ciscoPolicy, ciscoProducts=ciscoProducts)
