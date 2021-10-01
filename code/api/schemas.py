from marshmallow import ValidationError, Schema, fields


def validate_string(value):
    if value == '':
        raise ValidationError('Field may not be blank.')


class ObservableSchema(Schema):
    type = fields.String(
        validate=validate_string,
        required=True,
    )
    value = fields.String(
        validate=validate_string,
        required=True,
    )


class DashboardTileSchema(Schema):
    tile_id = fields.String(
        data_key='tile_id',
        validate=validate_string,
        required=True
    )


class DashboardTileDataSchema(Schema):
    period = fields.String(
        data_key='period',
        validate=validate_string,
        required=True
    )
    tile_id = fields.String(
        data_key='tile_id',
        validate=validate_string,
        required=True
    )
