"""Blender API utilities."""


import bpy

import mesh_mesh_align_plus.advanced_tools as maplus_adv_tools
import mesh_mesh_align_plus.align_points as maplus_apt
import mesh_mesh_align_plus.align_lines as maplus_aln
import mesh_mesh_align_plus.align_objects as maplus_aobjects
import mesh_mesh_align_plus.distribute_objects as maplus_dobjects
import mesh_mesh_align_plus.align_planes as maplus_apl
import mesh_mesh_align_plus.axis_rotate as maplus_axr
import mesh_mesh_align_plus.calculate_compose as maplus_calc_compose
import mesh_mesh_align_plus.directional_slide as maplus_ds
import mesh_mesh_align_plus.scale_match_edge as maplus_sme
import mesh_mesh_align_plus.utils.geom as maplus_geom
import mesh_mesh_align_plus.utils.gui_tools as maplus_guitools
import mesh_mesh_align_plus.utils.storage as maplus_storage


classes = (

    maplus_apt.MAPLUS_OT_AlignPointsBase,
    maplus_apt.MAPLUS_OT_AlignPointsObject,
    maplus_apt.MAPLUS_OT_QuickAlignPointsObject,
    maplus_apt.MAPLUS_OT_QuickAlignPointsObjectOrigin,
    maplus_apt.MAPLUS_OT_AlignPointsMeshSelected,
    maplus_apt.MAPLUS_OT_QuickAlignPointsMeshSelected,
    maplus_apt.MAPLUS_OT_AlignPointsWholeMesh,
    maplus_apt.MAPLUS_OT_QuickAlignPointsWholeMesh,
    maplus_apt.MAPLUS_OT_EasyAlignPoints,
    maplus_apt.MAPLUS_OT_ClearEasyAlignPoints,
    maplus_apt.MAPLUS_OT_ShowHideEasyApt,
    maplus_apt.MAPLUS_OT_ShowHideQuickApt,

    maplus_aln.MAPLUS_OT_AlignLinesBase,
    maplus_aln.MAPLUS_OT_AlignLinesObject,
    maplus_aln.MAPLUS_OT_QuickAlignLinesObject,
    maplus_aln.MAPLUS_OT_QuickAlignLinesObjectOrigin,
    maplus_aln.MAPLUS_OT_AlignLinesMeshSelected,
    maplus_aln.MAPLUS_OT_AlignLinesWholeMesh,
    maplus_aln.MAPLUS_OT_QuickAlignLinesMeshSelected,
    maplus_aln.MAPLUS_OT_QuickAlignLinesWholeMesh,
    maplus_aln.MAPLUS_OT_EasyAlignLines,
    maplus_aln.MAPLUS_OT_ClearEasyAlignLines,
    maplus_aln.MAPLUS_OT_ShowHideEasyAln,
    maplus_aln.MAPLUS_OT_ShowHideQuickAln,

    maplus_apl.MAPLUS_OT_AlignPlanesBase,
    maplus_apl.MAPLUS_OT_AlignPlanesObject,
    maplus_apl.MAPLUS_OT_QuickAlignPlanesObject,
    maplus_apl.MAPLUS_OT_QuickAlignPlanesObjectOrigin,
    maplus_apl.MAPLUS_OT_AlignPlanesMeshSelected,
    maplus_apl.MAPLUS_OT_AlignPlanesWholeMesh,
    maplus_apl.MAPLUS_OT_QuickAlignPlanesMeshSelected,
    maplus_apl.MAPLUS_OT_QuickAlignPlanesWholeMesh,
    maplus_apl.MAPLUS_OT_EasyAlignPlanes,
    maplus_apl.MAPLUS_OT_ClearEasyAlignPlanes,
    maplus_apl.MAPLUS_OT_ShowHideEasyApl,
    maplus_apl.MAPLUS_OT_ShowHideQuickApl,

    maplus_ds.MAPLUS_OT_DirectionalSlideBase,
    maplus_ds.MAPLUS_OT_DirectionalSlideObject,
    maplus_ds.MAPLUS_OT_QuickDirectionalSlideObject,
    maplus_ds.MAPLUS_OT_QuickDirectionalSlideObjectOrigin,
    maplus_ds.MAPLUS_OT_DirectionalSlideMeshSelected,
    maplus_ds.MAPLUS_OT_DirectionalSlideWholeMesh,
    maplus_ds.MAPLUS_OT_QuickDirectionalSlideMeshSelected,
    maplus_ds.MAPLUS_OT_QuickDirectionalSlideWholeMesh,

    maplus_sme.MAPLUS_OT_ScaleMatchEdgeBase,
    maplus_sme.MAPLUS_OT_ScaleMatchEdgeObject,
    maplus_sme.MAPLUS_OT_QuickScaleMatchEdgeObject,
    maplus_sme.MAPLUS_OT_QuickScaleMatchEdgeObjectOrigin,
    maplus_sme.MAPLUS_OT_ScaleMatchEdgeMeshSelected,
    maplus_sme.MAPLUS_OT_QuickScaleMatchEdgeMeshSelected,
    maplus_sme.MAPLUS_OT_ScaleMatchEdgeWholeMesh,
    maplus_sme.MAPLUS_OT_QuickScaleMatchEdgeWholeMesh,
    maplus_sme.MAPLUS_OT_EasyScaleMatchEdge,
    maplus_sme.MAPLUS_OT_ClearEasyScaleMatchEdge,
    maplus_sme.MAPLUS_OT_ShowHideEasySme,
    maplus_sme.MAPLUS_OT_ShowHideQuickSme,

    maplus_axr.MAPLUS_OT_AxisRotateBase,
    maplus_axr.MAPLUS_OT_AxisRotateObject,
    maplus_axr.MAPLUS_OT_QuickAxisRotateObject,
    maplus_axr.MAPLUS_OT_QuickAxisRotateObjectOrigin,
    maplus_axr.MAPLUS_OT_AxisRotateMeshSelected,
    maplus_axr.MAPLUS_OT_AxisRotateWholeMesh,
    maplus_axr.MAPLUS_OT_QuickAxisRotateMeshSelected,
    maplus_axr.MAPLUS_OT_QuickAxisRotateWholeMesh,

    maplus_aobjects.MAPLUS_OT_QuickAlignObjects,
    maplus_dobjects.MAPLUS_OT_QuickDistributeObjectsBetween,
    maplus_dobjects.MAPLUS_OT_QuickDistObjBetweenGrabStart,
    maplus_dobjects.MAPLUS_OT_QuickDistObjBetweenGrabEnd,
    maplus_dobjects.MAPLUS_OT_QuickDistributeObjectsAlongLine,

    maplus_calc_compose.MAPLUS_OT_CalcLineLengthBase,
    maplus_calc_compose.MAPLUS_OT_CalcLineLength,
    maplus_calc_compose.MAPLUS_OT_QuickCalcLineLength,
    maplus_calc_compose.MAPLUS_OT_CalcRotationalDiffBase,
    maplus_calc_compose.MAPLUS_OT_CalcRotationalDiff,
    maplus_calc_compose.MAPLUS_OT_QuickCalcRotationalDiff,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromOriginBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromOrigin,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineFromOrigin,
    maplus_calc_compose.MAPLUS_OT_ComposeNormalFromPlaneBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNormalFromPlane,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNormalFromPlane,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromPointBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromPoint,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineFromPoint,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineAtPointLocationBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineAtPointLocation,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineAtPointLocation,
    maplus_calc_compose.MAPLUS_OT_CalcDistanceBetweenPointsBase,
    maplus_calc_compose.MAPLUS_OT_CalcDistanceBetweenPoints,
    maplus_calc_compose.MAPLUS_OT_QuickCalcDistanceBetweenPoints,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromPointsBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineFromPoints,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineFromPoints,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineVectorAdditionBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineVectorAddition,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineVectorAddition,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineVectorSubtractionBase,
    maplus_calc_compose.MAPLUS_OT_ComposeNewLineVectorSubtraction,
    maplus_calc_compose.MAPLUS_OT_QuickComposeNewLineVectorSubtraction,
    maplus_calc_compose.MAPLUS_OT_ComposePointIntersectingLinePlaneBase,
    maplus_calc_compose.MAPLUS_OT_ComposePointIntersectingLinePlane,
    maplus_calc_compose.MAPLUS_OT_QuickComposePointIntersectingLinePlane,

    maplus_geom.MAPLUS_OT_GrabFromGeometryBase,
    maplus_geom.MAPLUS_OT_GrabSmeNumeric,
    maplus_geom.MAPLUS_OT_GrabAndSetItemKindBase,
    maplus_geom.MAPLUS_OT_GrabAverageLocationBase,
    maplus_geom.MAPLUS_OT_GrabNormalBase,
    maplus_geom.MAPLUS_OT_GrabFromCursorBase,
    maplus_geom.MAPLUS_OT_SendCoordToCursorBase,
    maplus_geom.MAPLUS_OT_GrabAllSlot1,
    maplus_geom.MAPLUS_OT_GrabAllSlot1Loc,
    maplus_geom.MAPLUS_OT_GrabAllSlot2,
    maplus_geom.MAPLUS_OT_GrabAllSlot2Loc,
    maplus_geom.MAPLUS_OT_GrabAllCalcResult,
    maplus_geom.MAPLUS_OT_GrabPointFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabPointFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabPointFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabPointFromCursor,
    maplus_geom.MAPLUS_OT_QuickAptSrcGrabPointFromCursor,
    maplus_geom.MAPLUS_OT_QuickAptDestGrabPointFromCursor,
    maplus_geom.MAPLUS_OT_GrabPointFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabPointFromActiveGlobal,
    maplus_geom.MAPLUS_OT_GrabPointSlot1,
    maplus_geom.MAPLUS_OT_GrabPointSlot1Loc,
    maplus_geom.MAPLUS_OT_GrabPointCalcResult,
    maplus_geom.MAPLUS_OT_GrabPointCalcResultLoc,
    maplus_geom.MAPLUS_OT_GrabPointSlot2,
    maplus_geom.MAPLUS_OT_GrabPointSlot2Loc,
    maplus_geom.MAPLUS_OT_PointGrabAvg,
    maplus_geom.MAPLUS_OT_LineStartGrabAvg,
    maplus_geom.MAPLUS_OT_LineEndGrabAvg,
    maplus_geom.MAPLUS_OT_PlaneAGrabAvg,
    maplus_geom.MAPLUS_OT_PlaneBGrabAvg,
    maplus_geom.MAPLUS_OT_PlaneCGrabAvg,
    maplus_geom.MAPLUS_OT_Slot1PointGrabAvg,
    maplus_geom.MAPLUS_OT_Slot2PointGrabAvg,
    maplus_geom.MAPLUS_OT_CalcResultPointGrabAvg,
    maplus_geom.MAPLUS_OT_QuickAptGrabAvgSrc,
    maplus_geom.MAPLUS_OT_QuickAptGrabAvgDest,
    maplus_geom.MAPLUS_OT_QuickAlignPointsGrabSrc,
    maplus_geom.MAPLUS_OT_QuickAlignPointsGrabDest,
    maplus_geom.MAPLUS_OT_QuickAlignPointsGrabSrcLoc,
    maplus_geom.MAPLUS_OT_QuickAlignPointsGrabDestLoc,
    maplus_geom.MAPLUS_OT_SendPointToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendPointToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendPointToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendPointToCursor,
    maplus_geom.MAPLUS_OT_QuickAptSrcSendPointToCursor,
    maplus_geom.MAPLUS_OT_QuickAptDestSendPointToCursor,
    maplus_geom.MAPLUS_OT_GrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineStartFromCursor,
    maplus_geom.MAPLUS_OT_GrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot2GrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot1GrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot2GrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot1GrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot2GrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot2GrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_CalcResultGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabAvgLineStart,
    maplus_geom.MAPLUS_OT_Slot2GrabAvgLineStart,
    maplus_geom.MAPLUS_OT_CalcResultGrabAvgLineStart,
    maplus_geom.MAPLUS_OT_Slot1GrabAvgLineEnd,
    maplus_geom.MAPLUS_OT_Slot2GrabAvgLineEnd,
    maplus_geom.MAPLUS_OT_CalcResultGrabAvgLineEnd,
    maplus_geom.MAPLUS_OT_QuickAlnGrabAvgSrcLineStart,
    maplus_geom.MAPLUS_OT_QuickAlnGrabAvgDestLineStart,
    maplus_geom.MAPLUS_OT_QuickAlnGrabAvgSrcLineEnd,
    maplus_geom.MAPLUS_OT_QuickAlnGrabAvgDestLineEnd,
    maplus_geom.MAPLUS_OT_QuickAxrGrabAvgSrcLineStart,
    maplus_geom.MAPLUS_OT_QuickAxrGrabAvgSrcLineEnd,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineGrabAvgSrcLineStart,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineGrabAvgSrcLineEnd,
    maplus_geom.MAPLUS_OT_QuickDsGrabAvgSrcLineStart,
    maplus_geom.MAPLUS_OT_QuickDsGrabAvgSrcLineEnd,
    maplus_geom.MAPLUS_OT_QuickSmeGrabAvgSrcLineStart,
    maplus_geom.MAPLUS_OT_QuickSmeGrabAvgDestLineStart,
    maplus_geom.MAPLUS_OT_QuickSmeGrabAvgSrcLineEnd,
    maplus_geom.MAPLUS_OT_QuickSmeGrabAvgDestLineEnd,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineStartFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineStartFromActiveGlobal,
    maplus_geom.MAPLUS_OT_SendLineStartToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendLineStartToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendLineEndToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendLineStartToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendLineEndToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickAlnSrcSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickAlnDestSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickAxrSrcSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickDsSrcSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickDsDestSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickSmeSrcSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_QuickSmeDestSendLineStartToCursor,
    maplus_geom.MAPLUS_OT_GrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineEndFromCursor,
    maplus_geom.MAPLUS_OT_GrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAlnSrcGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAlnDestGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAxrSrcGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDsSrcGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickDsDestGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickSmeSrcGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineEndFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickSmeDestGrabLineEndFromActiveGlobal,
    maplus_geom.MAPLUS_OT_SendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickAlnSrcSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickAlnDestSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickAxrSrcSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickDsSrcSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickDsDestSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickSmeSrcSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_QuickSmeDestSendLineEndToCursor,
    maplus_geom.MAPLUS_OT_GrabAllVertsLineLocal,
    maplus_geom.MAPLUS_OT_GrabAllVertsLineGlobal,
    maplus_geom.MAPLUS_OT_GrabLineSlot1,
    maplus_geom.MAPLUS_OT_GrabLineSlot1Loc,
    maplus_geom.MAPLUS_OT_GrabLineSlot2,
    maplus_geom.MAPLUS_OT_GrabLineSlot2Loc,
    maplus_geom.MAPLUS_OT_GrabLineCalcResult,
    maplus_geom.MAPLUS_OT_GrabLineCalcResultLoc,
    maplus_geom.MAPLUS_OT_GrabNormal,
    maplus_geom.MAPLUS_OT_Slot1GrabNormal,
    maplus_geom.MAPLUS_OT_Slot2GrabNormal,
    maplus_geom.MAPLUS_OT_CalcResultGrabNormal,
    maplus_geom.MAPLUS_OT_QuickAlnGrabNormalSrc,
    maplus_geom.MAPLUS_OT_QuickAlnGrabNormalDest,
    maplus_geom.MAPLUS_OT_QuickAxrGrabNormalSrc,
    maplus_geom.MAPLUS_OT_QuickDsGrabNormalSrc,
    maplus_geom.MAPLUS_OT_QuickSmeGrabNormalSrc,
    maplus_geom.MAPLUS_OT_QuickSmeGrabNormalDest,
    maplus_geom.MAPLUS_OT_QuickAlignLinesGrabSrc,
    maplus_geom.MAPLUS_OT_QuickAlignLinesGrabSrcLoc,
    maplus_geom.MAPLUS_OT_QuickAlignLinesGrabDest,
    maplus_geom.MAPLUS_OT_QuickAlignLinesGrabDestLoc,
    maplus_geom.MAPLUS_OT_QuickScaleMatchEdgeGrabSrc,
    maplus_geom.MAPLUS_OT_QuickScaleMatchEdgeGrabSrcLoc,
    maplus_geom.MAPLUS_OT_QuickScaleMatchEdgeGrabDest,
    maplus_geom.MAPLUS_OT_QuickScaleMatchEdgeGrabDestLoc,
    maplus_geom.MAPLUS_OT_QuickAxisRotateGrabSrc,
    maplus_geom.MAPLUS_OT_QuickAxisRotateGrabSrcLoc,
    maplus_geom.MAPLUS_OT_DistObjAlongLineGrabSrc,
    maplus_geom.MAPLUS_OT_DistObjAlongLineGrabSrcLoc,
    maplus_geom.MAPLUS_OT_QuickDirectionalSlideGrabSrc,
    maplus_geom.MAPLUS_OT_QuickDirectionalSlideGrabSrcLoc,
    maplus_geom.MAPLUS_OT_GrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneAFromCursor,
    maplus_geom.MAPLUS_OT_GrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot1GrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_Slot2GrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_CalcResultGrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_Slot1GrabAvgPlaneA,
    maplus_geom.MAPLUS_OT_Slot1GrabAvgPlaneB,
    maplus_geom.MAPLUS_OT_Slot1GrabAvgPlaneC,
    maplus_geom.MAPLUS_OT_Slot2GrabAvgPlaneA,
    maplus_geom.MAPLUS_OT_Slot2GrabAvgPlaneB,
    maplus_geom.MAPLUS_OT_Slot2GrabAvgPlaneC,
    maplus_geom.MAPLUS_OT_CalcResultGrabAvgPlaneA,
    maplus_geom.MAPLUS_OT_CalcResultGrabAvgPlaneB,
    maplus_geom.MAPLUS_OT_CalcResultGrabAvgPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgSrcPlaneA,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgDestPlaneA,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeGrabAvgDestPlaneA,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneAFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneAFromActiveGlobal,
    maplus_geom.MAPLUS_OT_SendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_Slot1SendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_Slot2SendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_CalcResultSendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcSendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestSendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSendPlaneAToCursor,
    maplus_geom.MAPLUS_OT_GrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneBFromCursor,
    maplus_geom.MAPLUS_OT_GrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgSrcPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgDestPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgSetOriginModeDestPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneBFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneBFromActiveGlobal,
    maplus_geom.MAPLUS_OT_SendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcSendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestSendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSendPlaneBToCursor,
    maplus_geom.MAPLUS_OT_GrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneCFromCursor,
    maplus_geom.MAPLUS_OT_GrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_GrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgSrcPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplGrabAvgDestPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeGrabAvgDestPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSrcGrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneCFromActiveLocal,
    maplus_geom.MAPLUS_OT_QuickAplDestGrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestGrabPlaneCFromActiveGlobal,
    maplus_geom.MAPLUS_OT_SendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSrcSendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_QuickAplDestSendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSendPlaneCToCursor,
    maplus_geom.MAPLUS_OT_GrabAllVertsPlaneLocal,
    maplus_geom.MAPLUS_OT_GrabAllVertsPlaneGlobal,
    maplus_geom.MAPLUS_OT_GrabPlaneSlot1Loc,
    maplus_geom.MAPLUS_OT_GrabPlaneSlot1,
    maplus_geom.MAPLUS_OT_GrabPlaneSlot2Loc,
    maplus_geom.MAPLUS_OT_GrabPlaneSlot2,
    maplus_geom.MAPLUS_OT_GrabPlaneCalcResultLoc,
    maplus_geom.MAPLUS_OT_GrabPlaneCalcResult,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesGrabSrc,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesGrabDest,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesSetOriginModeGrabDest,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesGrabSrcLoc,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesGrabDestLoc,
    maplus_geom.MAPLUS_OT_QuickAlignPlanesSetOriginModeGrabDestLoc,
    maplus_geom.MAPLUS_OT_SwapPointsBase,
    maplus_geom.MAPLUS_OT_SwapLinePoints,
    maplus_geom.MAPLUS_OT_Slot1SwapLinePoints,
    maplus_geom.MAPLUS_OT_Slot2SwapLinePoints,
    maplus_geom.MAPLUS_OT_CalcResultSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickAlnSrcSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickAlnDestSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickAxrSrcSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickDistObjAlongLineSrcSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickDsSrcSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickSmeSrcSwapLinePoints,
    maplus_geom.MAPLUS_OT_QuickSmeDestSwapLinePoints,
    maplus_geom.MAPLUS_OT_SwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_SwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_SwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_Slot1SwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_Slot1SwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_Slot1SwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_Slot2SwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_Slot2SwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_Slot2SwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_CalcResultSwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_CalcResultSwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_CalcResultSwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSrcSwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplSrcSwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSrcSwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplDestSwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSwapPlaneAPlaneB,
    maplus_geom.MAPLUS_OT_QuickAplDestSwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSwapPlaneAPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplDestSwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_QuickAplSetOriginModeDestSwapPlaneBPlaneC,
    maplus_geom.MAPLUS_OT_SetOtherComponentsBase,
    maplus_geom.MAPLUS_OT_ZeroOtherPointX,
    maplus_geom.MAPLUS_OT_ZeroOtherPointY,
    maplus_geom.MAPLUS_OT_ZeroOtherPointZ,
    maplus_geom.MAPLUS_OT_ZeroOtherLineStartX,
    maplus_geom.MAPLUS_OT_ZeroOtherLineStartY,
    maplus_geom.MAPLUS_OT_ZeroOtherLineStartZ,
    maplus_geom.MAPLUS_OT_ZeroOtherLineEndX,
    maplus_geom.MAPLUS_OT_ZeroOtherLineEndY,
    maplus_geom.MAPLUS_OT_ZeroOtherLineEndZ,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointAX,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointAY,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointAZ,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointBX,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointBY,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointBZ,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointCX,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointCY,
    maplus_geom.MAPLUS_OT_ZeroOtherPlanePointCZ,
    maplus_geom.MAPLUS_OT_OneOtherPointX,
    maplus_geom.MAPLUS_OT_OneOtherPointY,
    maplus_geom.MAPLUS_OT_OneOtherPointZ,
    maplus_geom.MAPLUS_OT_OneOtherLineStartX,
    maplus_geom.MAPLUS_OT_OneOtherLineStartY,
    maplus_geom.MAPLUS_OT_OneOtherLineStartZ,
    maplus_geom.MAPLUS_OT_OneOtherLineEndX,
    maplus_geom.MAPLUS_OT_OneOtherLineEndY,
    maplus_geom.MAPLUS_OT_OneOtherLineEndZ,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointAX,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointAY,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointAZ,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointBX,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointBY,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointBZ,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointCX,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointCY,
    maplus_geom.MAPLUS_OT_OneOtherPlanePointCZ,
    maplus_geom.MAPLUS_OT_ApplyGeomModifiers,
    maplus_geom.MAPLUS_OT_ShowHideQuickGeomBaseClass,
    maplus_geom.MAPLUS_OT_ShowHideQuickCalcSlot1Geom,
    maplus_geom.MAPLUS_OT_ShowHideQuickCalcSlot2Geom,
    maplus_geom.MAPLUS_OT_ShowHideQuickCalcResultGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAptSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAptDestGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAlnSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAlnDestGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAplSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAplDestGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAplSetOriginModeDestGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickAxrSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickDsSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickSmeSrcGeom,
    maplus_geom.MAPLUS_OT_ShowHideQuickSmeDestGeom,
    maplus_geom.MAPLUS_OT_ShowHideDistAlongLineGeom,

    maplus_storage.BasicVariant,
    maplus_storage.MAPlusPrimitive,
    maplus_storage.MAPlusData,
    maplus_storage.MAPLUS_OT_CopyToOtherBase,

    maplus_storage.MAPLUS_OT_PasteIntoAdvToolsActive,
    maplus_storage.MAPLUS_OT_CopyFromAdvToolsActive,
    maplus_storage.MAPLUS_OT_PasteIntoSlot1,
    maplus_storage.MAPLUS_OT_CopyFromSlot1,
    maplus_storage.MAPLUS_OT_PasteIntoSlot2,
    maplus_storage.MAPLUS_OT_CopyFromSlot2,
    maplus_storage.MAPLUS_OT_CopyFromCalcResult,
    maplus_storage.MAPLUS_OT_PasteIntoCalcResult,
    maplus_storage.MAPLUS_OT_PasteIntoAptSrc,
    maplus_storage.MAPLUS_OT_CopyFromAptSrc,
    maplus_storage.MAPLUS_OT_PasteIntoAptDest,
    maplus_storage.MAPLUS_OT_CopyFromAptDest,
    maplus_storage.MAPLUS_OT_PasteIntoAlnSrc,
    maplus_storage.MAPLUS_OT_CopyFromAlnSrc,
    maplus_storage.MAPLUS_OT_PasteIntoAlnDest,
    maplus_storage.MAPLUS_OT_CopyFromAlnDest,
    maplus_storage.MAPLUS_OT_PasteIntoAplSrc,
    maplus_storage.MAPLUS_OT_CopyFromAplSrc,
    maplus_storage.MAPLUS_OT_PasteIntoAplDest,
    maplus_storage.MAPLUS_OT_PasteIntoAplSetOriginModeDest,
    maplus_storage.MAPLUS_OT_CopyFromAplDest,
    maplus_storage.MAPLUS_OT_CopyFromAplSetOriginModeDest,
    maplus_storage.MAPLUS_OT_PasteIntoAxrSrc,
    maplus_storage.MAPLUS_OT_CopyFromAxrSrc,
    maplus_storage.MAPLUS_OT_PasteIntoDsSrc,
    maplus_storage.MAPLUS_OT_CopyFromDsSrc,
    maplus_storage.MAPLUS_OT_PasteIntoSmeSrc,
    maplus_storage.MAPLUS_OT_CopyFromSmeSrc,
    maplus_storage.MAPLUS_OT_PasteIntoSmeDest,
    maplus_storage.MAPLUS_OT_CopyFromSmeDest,

    maplus_adv_tools.MAPLUS_OT_AddListItemBase,
    maplus_adv_tools.MAPLUS_OT_AddNewPoint,
    maplus_adv_tools.MAPLUS_OT_AddNewLine,
    maplus_adv_tools.MAPLUS_OT_AddNewPlane,
    maplus_adv_tools.MAPLUS_OT_AddNewCalculation,
    maplus_adv_tools.MAPLUS_OT_AddNewTransformation,

    maplus_adv_tools.MAPLUS_OT_ChangeTypeBaseClass,
    maplus_adv_tools.MAPLUS_OT_ChangeTypeToPointPrim,
    maplus_adv_tools.MAPLUS_OT_ChangeTypeToLinePrim,
    maplus_adv_tools.MAPLUS_OT_ChangeTypeToPlanePrim,
    maplus_adv_tools.MAPLUS_OT_ChangeTypeToCalcPrim,
    maplus_adv_tools.MAPLUS_OT_ChangeTypeToTransfPrim,
    maplus_adv_tools.MAPLUS_OT_ChangeCalcBaseClass,
    maplus_adv_tools.MAPLUS_OT_ChangeCalcToSingle,
    maplus_adv_tools.MAPLUS_OT_ChangeCalcToMulti,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfBaseClass,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToAlignPoints,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToDirectionalSlide,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToScaleMatchEdge,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToAxisRotate,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToAlignLines,
    maplus_adv_tools.MAPLUS_OT_ChangeTransfToAlignPlanes,

    maplus_adv_tools.MAPLUS_OT_DuplicateItemBase,
    maplus_adv_tools.MAPLUS_OT_RemoveListItem,
    maplus_adv_tools.MAPLUS_OT_SpecialsAddFromActiveBase,
    maplus_adv_tools.MAPLUS_OT_SpecialsAddPointFromActiveGlobal,
    maplus_adv_tools.MAPLUS_OT_SpecialsAddLineFromActiveGlobal,
    maplus_adv_tools.MAPLUS_OT_SpecialsAddPlaneFromActiveGlobal,

    # GUI registration
    maplus_adv_tools.MAPLUS_UL_MAPlusList,
    maplus_adv_tools.MAPLUS_PT_MAPlusGui,

    maplus_apt.MAPLUS_PT_QuickAlignPointsGUI,
    maplus_aln.MAPLUS_PT_QuickAlignLinesGUI,
    maplus_apl.MAPLUS_PT_QuickAlignPlanesGUI,
    maplus_axr.MAPLUS_PT_QuickAxisRotateGUI,
    maplus_ds.MAPLUS_PT_QuickDirectionalSlideGUI,
    maplus_sme.MAPLUS_PT_QuickSMEGUI,
    maplus_aobjects.MAPLUS_PT_QuickAlignObjectsGUI,
    maplus_dobjects.MAPLUS_PT_QuickDistributeObjectsGUI,
    maplus_calc_compose.MAPLUS_PT_CalculateAndComposeGUI,

    # maplus_except.UniqueNameError,
    # maplus_except.NonMeshGrabError,
    # maplus_except.InsufficientSelectionError,
)


def register():
    # Make custom classes available inside blender via bpy.types
    for cls in classes:
        bpy.utils.register_class(cls)

    # Extend the scene class here to include the addon data
    bpy.types.Scene.maplus_data = bpy.props.PointerProperty(
        type=maplus_storage.MAPlusData
    )

    bpy.types.VIEW3D_MT_object_context_menu.append(maplus_guitools.specials_menu_items)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(maplus_guitools.specials_menu_items)


def unregister():
    del bpy.types.Scene.maplus_data
    bpy.types.VIEW3D_MT_object_context_menu.remove(maplus_guitools.specials_menu_items)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(maplus_guitools.specials_menu_items)

    # Remove custom classes from blender's bpy.types
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
