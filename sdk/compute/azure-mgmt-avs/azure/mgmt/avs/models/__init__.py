# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Addon
    from ._models_py3 import AddonHcxProperties
    from ._models_py3 import AddonList
    from ._models_py3 import AddonProperties
    from ._models_py3 import AddonSrmProperties
    from ._models_py3 import AddonVrProperties
    from ._models_py3 import AdminCredentials
    from ._models_py3 import AvailabilityProperties
    from ._models_py3 import Circuit
    from ._models_py3 import CloudLink
    from ._models_py3 import CloudLinkList
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterList
    from ._models_py3 import ClusterProperties
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import CommonClusterProperties
    from ._models_py3 import Datastore
    from ._models_py3 import DatastoreList
    from ._models_py3 import DiskPoolVolume
    from ._models_py3 import Encryption
    from ._models_py3 import EncryptionKeyVaultProperties
    from ._models_py3 import Endpoints
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExpressRouteAuthorization
    from ._models_py3 import ExpressRouteAuthorizationList
    from ._models_py3 import GlobalReachConnection
    from ._models_py3 import GlobalReachConnectionList
    from ._models_py3 import HcxEnterpriseSite
    from ._models_py3 import HcxEnterpriseSiteList
    from ._models_py3 import IdentitySource
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagementCluster
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NetAppVolume
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationList
    from ._models_py3 import OperationProperties
    from ._models_py3 import PSCredentialExecutionParameter
    from ._models_py3 import PlacementPoliciesList
    from ._models_py3 import PlacementPolicy
    from ._models_py3 import PlacementPolicyProperties
    from ._models_py3 import PlacementPolicyUpdate
    from ._models_py3 import PrivateCloud
    from ._models_py3 import PrivateCloudIdentity
    from ._models_py3 import PrivateCloudList
    from ._models_py3 import PrivateCloudProperties
    from ._models_py3 import PrivateCloudUpdate
    from ._models_py3 import PrivateCloudUpdateProperties
    from ._models_py3 import ProxyResource
    from ._models_py3 import Quota
    from ._models_py3 import Resource
    from ._models_py3 import ScriptCmdlet
    from ._models_py3 import ScriptCmdletsList
    from ._models_py3 import ScriptExecution
    from ._models_py3 import ScriptExecutionParameter
    from ._models_py3 import ScriptExecutionsList
    from ._models_py3 import ScriptPackage
    from ._models_py3 import ScriptPackagesList
    from ._models_py3 import ScriptParameter
    from ._models_py3 import ScriptSecureStringExecutionParameter
    from ._models_py3 import ScriptStringExecutionParameter
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import Trial
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineRestrictMovement
    from ._models_py3 import VirtualMachinesList
    from ._models_py3 import VmHostPlacementPolicyProperties
    from ._models_py3 import VmPlacementPolicyProperties
    from ._models_py3 import WorkloadNetworkDhcp
    from ._models_py3 import WorkloadNetworkDhcpEntity
    from ._models_py3 import WorkloadNetworkDhcpList
    from ._models_py3 import WorkloadNetworkDhcpRelay
    from ._models_py3 import WorkloadNetworkDhcpServer
    from ._models_py3 import WorkloadNetworkDnsService
    from ._models_py3 import WorkloadNetworkDnsServicesList
    from ._models_py3 import WorkloadNetworkDnsZone
    from ._models_py3 import WorkloadNetworkDnsZonesList
    from ._models_py3 import WorkloadNetworkGateway
    from ._models_py3 import WorkloadNetworkGatewayList
    from ._models_py3 import WorkloadNetworkPortMirroring
    from ._models_py3 import WorkloadNetworkPortMirroringList
    from ._models_py3 import WorkloadNetworkPublicIP
    from ._models_py3 import WorkloadNetworkPublicIPsList
    from ._models_py3 import WorkloadNetworkSegment
    from ._models_py3 import WorkloadNetworkSegmentPortVif
    from ._models_py3 import WorkloadNetworkSegmentSubnet
    from ._models_py3 import WorkloadNetworkSegmentsList
    from ._models_py3 import WorkloadNetworkVMGroup
    from ._models_py3 import WorkloadNetworkVMGroupsList
    from ._models_py3 import WorkloadNetworkVirtualMachine
    from ._models_py3 import WorkloadNetworkVirtualMachinesList
except (SyntaxError, ImportError):
    from ._models import Addon  # type: ignore
    from ._models import AddonHcxProperties  # type: ignore
    from ._models import AddonList  # type: ignore
    from ._models import AddonProperties  # type: ignore
    from ._models import AddonSrmProperties  # type: ignore
    from ._models import AddonVrProperties  # type: ignore
    from ._models import AdminCredentials  # type: ignore
    from ._models import AvailabilityProperties  # type: ignore
    from ._models import Circuit  # type: ignore
    from ._models import CloudLink  # type: ignore
    from ._models import CloudLinkList  # type: ignore
    from ._models import Cluster  # type: ignore
    from ._models import ClusterList  # type: ignore
    from ._models import ClusterProperties  # type: ignore
    from ._models import ClusterUpdate  # type: ignore
    from ._models import CommonClusterProperties  # type: ignore
    from ._models import Datastore  # type: ignore
    from ._models import DatastoreList  # type: ignore
    from ._models import DiskPoolVolume  # type: ignore
    from ._models import Encryption  # type: ignore
    from ._models import EncryptionKeyVaultProperties  # type: ignore
    from ._models import Endpoints  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExpressRouteAuthorization  # type: ignore
    from ._models import ExpressRouteAuthorizationList  # type: ignore
    from ._models import GlobalReachConnection  # type: ignore
    from ._models import GlobalReachConnectionList  # type: ignore
    from ._models import HcxEnterpriseSite  # type: ignore
    from ._models import HcxEnterpriseSiteList  # type: ignore
    from ._models import IdentitySource  # type: ignore
    from ._models import LogSpecification  # type: ignore
    from ._models import ManagementCluster  # type: ignore
    from ._models import MetricDimension  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import NetAppVolume  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import OperationProperties  # type: ignore
    from ._models import PSCredentialExecutionParameter  # type: ignore
    from ._models import PlacementPoliciesList  # type: ignore
    from ._models import PlacementPolicy  # type: ignore
    from ._models import PlacementPolicyProperties  # type: ignore
    from ._models import PlacementPolicyUpdate  # type: ignore
    from ._models import PrivateCloud  # type: ignore
    from ._models import PrivateCloudIdentity  # type: ignore
    from ._models import PrivateCloudList  # type: ignore
    from ._models import PrivateCloudProperties  # type: ignore
    from ._models import PrivateCloudUpdate  # type: ignore
    from ._models import PrivateCloudUpdateProperties  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Quota  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ScriptCmdlet  # type: ignore
    from ._models import ScriptCmdletsList  # type: ignore
    from ._models import ScriptExecution  # type: ignore
    from ._models import ScriptExecutionParameter  # type: ignore
    from ._models import ScriptExecutionsList  # type: ignore
    from ._models import ScriptPackage  # type: ignore
    from ._models import ScriptPackagesList  # type: ignore
    from ._models import ScriptParameter  # type: ignore
    from ._models import ScriptSecureStringExecutionParameter  # type: ignore
    from ._models import ScriptStringExecutionParameter  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import Trial  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineRestrictMovement  # type: ignore
    from ._models import VirtualMachinesList  # type: ignore
    from ._models import VmHostPlacementPolicyProperties  # type: ignore
    from ._models import VmPlacementPolicyProperties  # type: ignore
    from ._models import WorkloadNetworkDhcp  # type: ignore
    from ._models import WorkloadNetworkDhcpEntity  # type: ignore
    from ._models import WorkloadNetworkDhcpList  # type: ignore
    from ._models import WorkloadNetworkDhcpRelay  # type: ignore
    from ._models import WorkloadNetworkDhcpServer  # type: ignore
    from ._models import WorkloadNetworkDnsService  # type: ignore
    from ._models import WorkloadNetworkDnsServicesList  # type: ignore
    from ._models import WorkloadNetworkDnsZone  # type: ignore
    from ._models import WorkloadNetworkDnsZonesList  # type: ignore
    from ._models import WorkloadNetworkGateway  # type: ignore
    from ._models import WorkloadNetworkGatewayList  # type: ignore
    from ._models import WorkloadNetworkPortMirroring  # type: ignore
    from ._models import WorkloadNetworkPortMirroringList  # type: ignore
    from ._models import WorkloadNetworkPublicIP  # type: ignore
    from ._models import WorkloadNetworkPublicIPsList  # type: ignore
    from ._models import WorkloadNetworkSegment  # type: ignore
    from ._models import WorkloadNetworkSegmentPortVif  # type: ignore
    from ._models import WorkloadNetworkSegmentSubnet  # type: ignore
    from ._models import WorkloadNetworkSegmentsList  # type: ignore
    from ._models import WorkloadNetworkVMGroup  # type: ignore
    from ._models import WorkloadNetworkVMGroupsList  # type: ignore
    from ._models import WorkloadNetworkVirtualMachine  # type: ignore
    from ._models import WorkloadNetworkVirtualMachinesList  # type: ignore

from ._avs_client_enums import (
    AddonProvisioningState,
    AddonType,
    AffinityType,
    AvailabilityStrategy,
    CloudLinkStatus,
    ClusterProvisioningState,
    DatastoreProvisioningState,
    DatastoreStatus,
    DhcpTypeEnum,
    DnsServiceLogLevelEnum,
    DnsServiceStatusEnum,
    EncryptionKeyStatus,
    EncryptionState,
    EncryptionVersionType,
    ExpressRouteAuthorizationProvisioningState,
    GlobalReachConnectionProvisioningState,
    GlobalReachConnectionStatus,
    HcxEnterpriseSiteStatus,
    InternetEnum,
    MountOptionEnum,
    OptionalParamEnum,
    PlacementPolicyProvisioningState,
    PlacementPolicyState,
    PlacementPolicyType,
    PortMirroringDirectionEnum,
    PortMirroringStatusEnum,
    PrivateCloudProvisioningState,
    QuotaEnabled,
    ResourceIdentityType,
    ScriptExecutionParameterType,
    ScriptExecutionProvisioningState,
    ScriptOutputStreamType,
    ScriptParameterTypes,
    SegmentStatusEnum,
    SslEnum,
    TrialStatus,
    VMGroupStatusEnum,
    VMTypeEnum,
    VirtualMachineRestrictMovementState,
    VisibilityParameterEnum,
    WorkloadNetworkDhcpProvisioningState,
    WorkloadNetworkDnsServiceProvisioningState,
    WorkloadNetworkDnsZoneProvisioningState,
    WorkloadNetworkPortMirroringProvisioningState,
    WorkloadNetworkPublicIPProvisioningState,
    WorkloadNetworkSegmentProvisioningState,
    WorkloadNetworkVMGroupProvisioningState,
)

__all__ = [
    'Addon',
    'AddonHcxProperties',
    'AddonList',
    'AddonProperties',
    'AddonSrmProperties',
    'AddonVrProperties',
    'AdminCredentials',
    'AvailabilityProperties',
    'Circuit',
    'CloudLink',
    'CloudLinkList',
    'Cluster',
    'ClusterList',
    'ClusterProperties',
    'ClusterUpdate',
    'CommonClusterProperties',
    'Datastore',
    'DatastoreList',
    'DiskPoolVolume',
    'Encryption',
    'EncryptionKeyVaultProperties',
    'Endpoints',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ExpressRouteAuthorization',
    'ExpressRouteAuthorizationList',
    'GlobalReachConnection',
    'GlobalReachConnectionList',
    'HcxEnterpriseSite',
    'HcxEnterpriseSiteList',
    'IdentitySource',
    'LogSpecification',
    'ManagementCluster',
    'MetricDimension',
    'MetricSpecification',
    'NetAppVolume',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'OperationProperties',
    'PSCredentialExecutionParameter',
    'PlacementPoliciesList',
    'PlacementPolicy',
    'PlacementPolicyProperties',
    'PlacementPolicyUpdate',
    'PrivateCloud',
    'PrivateCloudIdentity',
    'PrivateCloudList',
    'PrivateCloudProperties',
    'PrivateCloudUpdate',
    'PrivateCloudUpdateProperties',
    'ProxyResource',
    'Quota',
    'Resource',
    'ScriptCmdlet',
    'ScriptCmdletsList',
    'ScriptExecution',
    'ScriptExecutionParameter',
    'ScriptExecutionsList',
    'ScriptPackage',
    'ScriptPackagesList',
    'ScriptParameter',
    'ScriptSecureStringExecutionParameter',
    'ScriptStringExecutionParameter',
    'ServiceSpecification',
    'Sku',
    'TrackedResource',
    'Trial',
    'VirtualMachine',
    'VirtualMachineRestrictMovement',
    'VirtualMachinesList',
    'VmHostPlacementPolicyProperties',
    'VmPlacementPolicyProperties',
    'WorkloadNetworkDhcp',
    'WorkloadNetworkDhcpEntity',
    'WorkloadNetworkDhcpList',
    'WorkloadNetworkDhcpRelay',
    'WorkloadNetworkDhcpServer',
    'WorkloadNetworkDnsService',
    'WorkloadNetworkDnsServicesList',
    'WorkloadNetworkDnsZone',
    'WorkloadNetworkDnsZonesList',
    'WorkloadNetworkGateway',
    'WorkloadNetworkGatewayList',
    'WorkloadNetworkPortMirroring',
    'WorkloadNetworkPortMirroringList',
    'WorkloadNetworkPublicIP',
    'WorkloadNetworkPublicIPsList',
    'WorkloadNetworkSegment',
    'WorkloadNetworkSegmentPortVif',
    'WorkloadNetworkSegmentSubnet',
    'WorkloadNetworkSegmentsList',
    'WorkloadNetworkVMGroup',
    'WorkloadNetworkVMGroupsList',
    'WorkloadNetworkVirtualMachine',
    'WorkloadNetworkVirtualMachinesList',
    'AddonProvisioningState',
    'AddonType',
    'AffinityType',
    'AvailabilityStrategy',
    'CloudLinkStatus',
    'ClusterProvisioningState',
    'DatastoreProvisioningState',
    'DatastoreStatus',
    'DhcpTypeEnum',
    'DnsServiceLogLevelEnum',
    'DnsServiceStatusEnum',
    'EncryptionKeyStatus',
    'EncryptionState',
    'EncryptionVersionType',
    'ExpressRouteAuthorizationProvisioningState',
    'GlobalReachConnectionProvisioningState',
    'GlobalReachConnectionStatus',
    'HcxEnterpriseSiteStatus',
    'InternetEnum',
    'MountOptionEnum',
    'OptionalParamEnum',
    'PlacementPolicyProvisioningState',
    'PlacementPolicyState',
    'PlacementPolicyType',
    'PortMirroringDirectionEnum',
    'PortMirroringStatusEnum',
    'PrivateCloudProvisioningState',
    'QuotaEnabled',
    'ResourceIdentityType',
    'ScriptExecutionParameterType',
    'ScriptExecutionProvisioningState',
    'ScriptOutputStreamType',
    'ScriptParameterTypes',
    'SegmentStatusEnum',
    'SslEnum',
    'TrialStatus',
    'VMGroupStatusEnum',
    'VMTypeEnum',
    'VirtualMachineRestrictMovementState',
    'VisibilityParameterEnum',
    'WorkloadNetworkDhcpProvisioningState',
    'WorkloadNetworkDnsServiceProvisioningState',
    'WorkloadNetworkDnsZoneProvisioningState',
    'WorkloadNetworkPortMirroringProvisioningState',
    'WorkloadNetworkPublicIPProvisioningState',
    'WorkloadNetworkSegmentProvisioningState',
    'WorkloadNetworkVMGroupProvisioningState',
]
