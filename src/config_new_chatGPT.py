LOC = 'tum'

FIGSIZE = (14,6)

BAROCORRECTED_OUTPUT_FN = '{site}_{year}_barocorrected_{segment}.csv'

NORMALIZED_FN = '{sensor_type}_{sitename}_{year}.csv'

VENTED_OUTPUT_FN = '{site}_{span}_vented_{segment}.csv'

FINAL_OUTPUT_FN = '{site}_timeseries_stage_Q_T_{start}_{end}.csv'

FINAL_OUTPUT_METADATA_FN = '{site}_timeseries_stage_Q_T_{start}_{end}_metadata.txt'

SITE_SHORTNAME = {0 : 'LyellBlwMaclure',
                  1 : 'LyellAbvTB',
                  2 : 'DanaFk@BugCamp',
                  3 : 'Tuolumne@120',
                  4 : 'BuddCreek',
                  5 : 'DelaneyAbvPCT'}

SITE_LONGNAME = {0 : 'Lyell Below Maclure',
                 1 : 'Lyell Above Twin Bridges',
                 2 : 'Dana Fork at Bug Camp',
                 3 : 'Tuolumne River at 120',
                 4 : 'Budd Creek',
                 5 : 'Delaney Above PCT'}

LEVEL_HEADER = ['lvl_cm', 'temp_C']

BARO_HEADER = ['baro_cm', 'temp_C']

BARO_CORRECTED_HEADER = ['date_time(UTC:PDT+7)', 'raw_pressure(cm)', 'barocorrected_pressure(cm)', 'water_temperature(deg_C)', 'discharge_flag']

VENTED_CORRECTED_HEADER = ['date_time(UTC:PDT+7)', 'vented_pressure(cm)', 'water_temperature(deg_C)', 'discharge_flag']

NCAR_BARO_HEADER = ['baro_cm']

FINAL_OUTPUT_HEADER = ['date_time(UTC:PDT+7)', 'raw_pressure(cm)', 'barocorrected_pressure(cm)', 'adjusted_stage(cm)', 'estimated_discharge(cms)', 'water_temperature(deg_C)', 'discharge_flag']

NCAR_TUM_LAT = 37.5 # degrees N
NCAR_TUM_LON = 240 # degrees e

TUM_ELEVATION = 2627 # m

ANOMOLY_FLAG = 1
ICEJAM_FLAG = 2
MALFUNCTION_FLAG = 3


import numpy as np 

_safe_power = lambda base, exp: np.power(np.maximum(base, 0), exp)

RATING_CURVES = {
    0: (lambda h: np.where(
        h < 2.29893,
        5.08516 * _safe_power(h - 1.9383, 1.49088),
        20.1140 * _safe_power(h - 2.1167, 1.70046)
    )),

    1: (lambda h: np.where(
        h < 0.545817,
        13.0679 * _safe_power(h - 0.189547, 1.53746),
        np.where(
            h > 0.786625,
            34.0175 * _safe_power(h - 0.3297, 1.69602),
            32.3266 * _safe_power(h - 0.3171, 1.68957)
        )
    )),

    2: (lambda h: np.where(
        h < 0.354118,
        9.81848 * _safe_power(h - 0.218727, 1.48825),
        np.where(
            h > 0.904318,
            66.8344 * _safe_power(h - 0.4724, 1.68704),
            34.8425 * _safe_power(h - 0.2816, 1.6152)
        )
    )),

    3: (lambda h: np.where(
        h < 0.8011,
        34.3522 * _safe_power(h - 0.7639, 1.465),
        17.0873 * _safe_power(h - 0.7076, 1.7401)
    )),

    4: None,
    5: None
}