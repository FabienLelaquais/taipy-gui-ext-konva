// Stage.jsx
//
import { useMemo } from "react";
import { Stage as KonvaStage, Layer, Shape, Rect, Text } from "react-konva";

import { useDynamicProperty } from "taipy-gui";

interface StageProps {
  layers?: Array<Record<string, any>>;
  defaultLayers?: string;
}

const knownShapeTypes: Set<string> = new Set(["Rect", "Text"]);


const renderShapes = (shapes: Array<Record<string, any>>) =>
  shapes.map((shape, key) => {
    if (knownShapeTypes.has(shape.type)) {
      return <shape.type key={key} {...shape.p} />;
    }
    else {
      return null;
    }
  });

export default function Stage(props: StageProps) {
  const layers: Array<Record<string, any>> = useMemo(() => {
    if (props.layers) {
      return props.layers;
    } else if (props.defaultLayers) {
      try {
        return JSON.parse(props.defaultLayers).map(JSON.parse);
      } catch {
        console.error("Konva Scene: Failed to parse defaultLayers");
      }
    }
    return undefined;
  }, [props.layers, props.defaultLayers]);

  // Display the reversed text content
  return (
    <KonvaStage width={500} height={500}>
      {layers.map((layer, i) => (
        <Layer key={i}>{renderShapes(layer.shapes)}</Layer>
      ))}
    </KonvaStage>
  );
}
